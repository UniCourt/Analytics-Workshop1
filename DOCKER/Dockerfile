FROM gcc:latest
COPY . /usr/src/cpp_test
WORKDIR /usr/src/cpp_test
RUN g++ -o demo main.cpp
CMD [ "./demo" ]
