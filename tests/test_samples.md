# Test Results

Python version used: ______

Operating system: Android

Date: ______

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | ______ | ______ |
| 2 | http://192.0.2.10/account | IP address + HTTP | ______ | ______ |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | ______ | ______ |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | ______ | ______ |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | ______ | ______ |

## Notes

1. I learned how to identify warning signs in URLs.
2. I understood that no warning signs does not mean a URL is safe.
