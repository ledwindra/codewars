![Build](https://github.com/ledwindra/codewars/workflows/Build/badge.svg?branch=master)

# About this Repository

Hello, :earth_asia:!

[Codewars](https://www.codewars.com/) is an educational community for :computer: programming. It provides :question: :pencil: :dart: on many programming languages. Currently, I am using Python >= 3.6.0 :snake: to solve the problems. No third party module is required besides `pytest`. Note that they are not the best solutions ever made. My key interest include algorithms, data structures, and object oriented programming.

See my public profile [here](https://www.codewars.com/users/lukmanedwindra)

# Clone

```
cd ~
git clone https://github.com/ledwindra/codewars.git
cd codewars/
```

# Use virtual environment

```
python3 -m venv venv-codewars
source venv-codewars/bin/activate
pip3 install pytest
```

Run `deactivate` to exit from virtual environment.

# Contribute

Install `hub` command line in order to be able to pull request ([link](https://github.com/github/hub)).

```
git checkout -b [YOUR-BRANCH]
git pull origin master
git add .
git commit -m "[YOUR COMMIT MESSAGE]"
git push origin [YOUR-BRANCH]
hub pull-request https://github.com/ledwindra/codewars.git -m "[TITLE]"
```

# Run test

Before contributing, run the following test on your local machine.

```
pytest python
```

If passed the tests, it can be merged to the `master` branch.

Thanks for reading and happy coding! :sunglasses:
