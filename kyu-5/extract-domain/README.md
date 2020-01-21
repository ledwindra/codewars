# About

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```

# Test

```
python3 -m unittest test_extract_domain.py
```

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

