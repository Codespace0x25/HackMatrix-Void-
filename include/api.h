#ifndef __API_H__
#define __API_H__
#include <zmq/zmq.hpp>
#include <string>
#include "world.h"

using namespace std;

class Api {
  zmq::context_t context;
  zmq::socket_t socket;
  void initZmq(string bindAddress);
 public:
  Api(std::string bindAddress);
  void pollFor(World* world);
  void initWorld(World*, string );
};

#endif
