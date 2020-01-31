![Test](https://github.com/ledwindra/codewars/workflows/Test/badge.svg)

# About this Repository

Hello, :earth_asia:!

[Codewars](https://www.codewars.com/) is an educational community for :computer: programming. It provides :question: :pencil: :dart: on many programming languages. Currently, I am using Python :snake: and Ruby :gem: to solve the problems. No third party module is required besides `pytest`. Note that they are not the best solutions ever made. My key interest include algorithms, data structures, and object oriented programming.

See my public profile [here](https://www.codewars.com/users/lukmanedwindra)

# Clone

```
cd ~
git clone https://github.com/ledwindra/codewars.git
cd codewars/
```

# Python

## Use virtual environment

```
python3 -m venv venv-codewars
source venv-codewars/bin/activate
pip3 install pytest
```

Run `deactivate` to exit from virtual environment.

## Run test

Before contributing, run the following test on your local machine.

```
pytest python
```
# Ruby

[TO-DO]

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

If passed the tests, it can be merged to the `master` branch.

Thanks for reading and happy coding! :sunglasses:
