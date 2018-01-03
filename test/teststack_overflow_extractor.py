"""
Unittesting stack_overflow_extractor
"""
import unittest
import urllib
import requests
import validators
import stack_overflow_extractor as s


class Teststackoverflowextractor(unittest.TestCase):
    """
    contains test functions for that of stack_overflow_extractor functions
    """

    def setUp(self):
        """
        sets up test cases for testing the functions.
        :return: none
        """
        self.url1 = "https://stackoverflow.com/users/7690738/ashish-cherian"
        self.url2 = "https://stackoverflow.com/users/157247/t-j-crowder"
        self.user1, self.description1, self.tags1, self.links1 = s.stackoverflow(self.url1)
        self.repos1 = s.git_repos(self.links1)
        self.user2, self.description2, self.tags2, self.links2 = s.stackoverflow(self.url2)
        self.repos2 = s.git_repos(self.links2)

    def test_stackoverflow(self):
        """
        This function is used to test stackoverflow function
        which returns user name, description, tags and links.

        ...If url is valid

        https://stackoverflow.com/users/7690738/ashish-cherian

        returns username, description, tags and links

        ...If url is empty

        raise ValueError("unknown url type: %r" % self.full_url)

        ValueError: unknown url type: ''

        ...If an invalid url is given

        raise URLError(err)

        urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>

        :return: if test is ok or not
        """
        #validating url

        self.assertTrue(validators.url(self.url1))
        self.assertTrue(validators.url(self.url2))

        #checking if url is a stackoverflow url or not

        self.assertTrue("https://stackoverflow.com/users" in self.url1)
        self.assertTrue("https://stackoverflow.com/users" in self.url2)

        #checking connection to url

        self.assertEqual(urllib.request.urlopen(self.url1).getcode(), 200)
        self.assertEqual(urllib.request.urlopen(self.url2).getcode(), 200)

        #checking if url is not empty

        self.assertNotEqual(self.url1, "")
        self.assertNotEqual(self.url2, "")

        #checking for timeout error

        self.assertTrue(requests.get(self.url1, timeout=10.0))
        self.assertTrue(requests.get(self.url1, timeout=10.0))

        #checking username and description are not empty

        self.assertNotEqual(self.user1, "")
        self.assertNotEqual(self.description1, "")
        self.assertNotEqual(self.user2, "")
        self.assertNotEqual(self.description2, "")

    def test_git_repos(self):
        """
        This function is used to test git_repos.
        :return: if test is ok or not
        """
        self.assertTrue("github" in self.links1[i] for i in range(len(self.links1)))
        self.assertTrue("github" in self.links2[i] for i in range(len(self.links2)))

    def tearDown(self):
        """
        used to teardown the content setup bu setup function.
        :return: none
        """
        pass

if __name__ == "__main__":
    unittest.main()
