import unittest
import stack_overflow_extractor

class Teststack_overflow_extractor(unittest.TestCase):

    def setUp(self):

        self.user1, self.description1, self.tags1, self.links1 = stack_overflow_extractor.stackoverflow("https://stackoverflow.com/users/7690738/ashish-cherian")
        self.repos1 = stack_overflow_extractor.git_repos(self.links1)
        self.user2, self.description2, self.tags2, self.links2 = stack_overflow_extractor.stackoverflow("https://stackoverflow.com/users/157247/t-j-crowder")
        self.repos2 = stack_overflow_extractor.git_repos(self.links2)
        
    def test_stackoverflow(self):
        
        self.assertNotEqual(self.user1, "")
        self.assertNotEqual(self.description1, "")
        self.assertNotEqual(self.user2, "")
        self.assertNotEqual(self.description2, "")

    def test_git_repos(self):

        self.assertTrue("github" in self.links1[i] for i in range(len(self.links1)))
        self.assertTrue("github" in self.links2[i] for i in range(len(self.links2)))
        
    def tearDown(self):

        pass

if __name__ == "__main__":
    unittest.main()
