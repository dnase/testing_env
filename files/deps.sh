add-apt-repository -y ppa:bitcoin/bitcoin
apt-get update
# general dependencies
apt-get -y install git
apt-get -y install build-essential libtool automake autotools-dev autoconf pkg-config libssl-dev libgmp3-dev libevent-dev bsdmainutils libc6-dev-i386
apt-get -y install libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev
apt-get -y install libboost-all-dev
apt-get install -y libdb6.0-dev libdb6.0++-dev
apt-get install -y libminiupnpc-dev libzmq3-dev
# dependencies for compiling on Windows
apt-get install -y g++-mingw-w64-i686 mingw-w64-i686-dev g++-mingw-w64-x86-64 mingw-w64-x86-64-dev
apt-get install -y qtcreator qttools5-dev-tools
git clone https://github.com/DrumpfCore/Drumpfcoin.git /root/drumpfcode
cd /root/drumpfcode
git checkout drumpf2
