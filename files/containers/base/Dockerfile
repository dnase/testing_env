FROM ubuntu:xenial

RUN ["/bin/bash", "-c", "apt-get update"]
RUN ["/bin/bash", "-c", "apt-get install -y libzmq3-dev libminiupnpc-dev libssl-dev libevent-dev libgmp-dev git"]
RUN ["/bin/bash", "-c", "apt-get install -y build-essential libtool autotools-dev automake pkg-config"]
RUN ["/bin/bash", "-c", "apt-get install -y libssl-dev libevent-dev bsdmainutils software-properties-common"]
RUN ["/bin/bash", "-c", "apt-get -y install libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev libboost-all-dev"]
RUN ["/bin/bash", "-c", "add-apt-repository ppa:bitcoin/bitcoin"]
RUN ["/bin/bash", "-c", "apt-get update"]
RUN ["/bin/bash", "-c", "apt-get install libdb4.8-dev libdb4.8++-dev wget -y"]

CMD ["/bin/bash"]
