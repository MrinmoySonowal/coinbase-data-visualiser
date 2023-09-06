import concurrent.futures
import unittest
from datetime import datetime
from example_client import get_product_ids, get_candles


SECONDS_IN_A_MINUTE = 60


class TestClientServer(unittest.TestCase):
    def test_single_client(self):
        ids = get_product_ids()
        self.assertIsNotNone(ids)
        self.assertIsInstance(ids, list)
        self.assertGreater(len(ids), 0)

    def test_high_load_on_server(self):
        ids = [set(get_product_ids()) for _ in range(20)]
        self.assertTrue(all([id_list == ids[0] for id_list in ids]))

    def test_concurrent_client_requests(self):
        num_clients = 50
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_clients) as executor:
            results = [executor.submit(get_product_ids) for _ in range(num_clients)]
            ids = []
            for f in concurrent.futures.as_completed(results):
                ids.append(set(f.result()))
            self.assertEqual(len(ids), num_clients, "Expected 5 client results!")
            self.assertTrue(all([id_list == ids[0] and len(id_list) == len(ids[0]) for id_list in ids]))

    def test_candles_return_types_lengths(self):
        end_timestamp = int(datetime.now().timestamp())
        number_of_intervals = 10
        start_timestamp = int(end_timestamp - number_of_intervals*SECONDS_IN_A_MINUTE)
        granularity = 60
        candles = get_candles("BTC-USD", start_timestamp, end_timestamp, granularity)
        self.assertEqual(len(candles[0]), 6)
        self.assertTrue(len(candles)==number_of_intervals or len(candles)==number_of_intervals-1)
        self.assertEqual(type(candles), list)
        self.assertEqual(type(candles[0]), list)
        self.assertEqual(type(candles[0][0]), int)
        for i in range(1,6):
            self.assertEqual(type(candles[0][i]), float)


    def test_candles_on_known_values(self):
        # Note: I have checked the values using the following endpoint from the coin base server:
        # https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=60&start=1693962540&end=1693962600
        end_timestamp = 1693962600
        start_timestamp = 1693962540
        granularity = 60
        candles = get_candles("BTC-USD", start_timestamp, end_timestamp, granularity)
        self.assertEqual(len(candles[0]), 6)
        self.assertEqual(candles[0][0], end_timestamp)
        self.assertEqual(candles[1][0], start_timestamp)
        low_on_end_time = candles[0][1]
        self.assertEqual(low_on_end_time, 25799.12)
        high_on_end_time = candles[0][2]
        self.assertEqual(high_on_end_time, 25803.33)

    def test_in_range_candles(self):
        end_timestamp = int(datetime.now().timestamp())
        number_of_intervals = 40
        self.assertLessEqual(number_of_intervals, 300, "Please set number_of_intervals to be less than or equal to 300")
        start_timestamp = int(end_timestamp - number_of_intervals * SECONDS_IN_A_MINUTE)
        granularity = 60
        candles = get_candles("BTC-USD", start_timestamp, end_timestamp, granularity)
        self.assertEqual(len(candles[0]), 6)
        self.assertTrue(len(candles) == number_of_intervals or len(candles) == number_of_intervals - 1)

    def test_out_of_range_candles(self):
        end_timestamp = int(datetime.now().timestamp())
        number_of_intervals = 350
        self.assertGreater(number_of_intervals, 300)
        start_timestamp = int(end_timestamp - number_of_intervals * SECONDS_IN_A_MINUTE)
        granularity = 60
        candles = get_candles("BTC-USD", start_timestamp, end_timestamp, granularity)
        self.assertEqual(len(candles[0]), 6)
        self.assertTrue(len(candles) == number_of_intervals or len(candles) == number_of_intervals - 1)






if __name__ == "__main__":
    unittest.main()
