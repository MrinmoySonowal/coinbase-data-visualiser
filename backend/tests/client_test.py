import concurrent.futures
import unittest
from example_client import get_product_ids


class TestClientServer(unittest.TestCase):
    def test_single_client(self):
        ids = get_product_ids()
        self.assertIsNotNone(ids)
        self.assertIsInstance(ids, list)
        self.assertGreater(len(ids), 0)

    def test_multiple_clients(self):
        ids1 = get_product_ids()
        ids2 = get_product_ids()
        self.assertEqual(set(ids1), set(ids2))

    def test_high_load_on_server(self):
        ids = [set(get_product_ids()) for _ in range(20)]
        self.assertTrue(all([id_list == ids[0] for id_list in ids]))

    def test_parallel_clients(self):
        num_clients = 5
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_clients) as executor:
            results = [executor.submit(get_product_ids) for _ in range(num_clients)]
            ids = []
            for f in concurrent.futures.as_completed(results):
                ids.append(set(f.result()))
            self.assertEqual(len(ids), 5, "Expected 5 client results!")
            self.assertTrue(all([id_list == ids[0] and len(id_list) == len(ids[0]) for id_list in ids]))


if __name__ == "__main__":
    unittest.main()
