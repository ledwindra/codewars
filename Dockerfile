FROM python:3

# Setup a spot for the code
WORKDIR /codewars

# Upgrade pip
RUN pip3 install --upgrade pip

# make sure that pytest is installed
# we'll need it to run the tests!
RUN pip3 install pytest

# Copy over the source code (!modify this section!)
# If you have other code here you need to copy it too
COPY python python/

CMD ["/bin/bash"]
