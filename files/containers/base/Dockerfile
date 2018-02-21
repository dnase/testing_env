FROM ubuntu:xenial

RUN ["/bin/bash", "-c", "apt-get update -y"]
RUN ["/bin/bash", "-c", "apt-get upgrade -y"]
RUN ["/bin/bash", "-c", "apt-get dist-upgrade -y"]
RUN ["/bin/bash", "-c", "apt-get install htop git wget -y"]
RUN ["/bin/bash", "-c", "apt-get install build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils software-properties-common libgmp3-dev  -y"]
RUN ["/bin/bash", "-c", "apt-get install libboost-all-dev -y"]
RUN ["/bin/bash", "-c", "add-apt-repository ppa:bitcoin/bitcoin -y"]
RUN ["/bin/bash", "-c", "apt-get update -y"]
RUN ["/bin/bash", "-c", "apt-get install libdb4.8-dev libdb4.8++-dev -y"]
RUN ["/bin/bash", "-c", "apt-get install libminiupnpc-dev -y"]

CMD ["/bin/bash"]
