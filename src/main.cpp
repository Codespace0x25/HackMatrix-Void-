#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "renderer.h"
#include <zmq/zmq.hpp>
#include <glm/glm.hpp>

void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
  glViewport(0, 0, width, height);
}

void testZmq() {
  zmq::context_t ctx;
  zmq::socket_t sock(ctx, zmq::socket_type::push);
  sock.bind("inproc://test");
  sock.send(zmq::str_buffer("Hello, world"), zmq::send_flags::dontwait);
}

GLFWwindow* init() {
  glfwInit();
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
  GLFWwindow* window = glfwCreateWindow(800, 600, "matrix", NULL, NULL);
  if (window == NULL) {
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return NULL;
  }
  glfwMakeContextCurrent(window);

  if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
    std::cout << "Failed to initialize GLAD" << std::endl;
    return NULL;
  }
  glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
  return window;
}

void handleEscape(GLFWwindow* window) {
  if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
    glfwSetWindowShouldClose(window, true);
  }
}

void handleControls(GLFWwindow* window, Camera* camera) {

  bool up = glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS;
  bool down = glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS;
  bool left = glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS;
  bool right = glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS;
  camera->handleTranslateForce(up,down,left,right);
}

void loop (GLFWwindow* window, Renderer* renderer, Camera* camera) {
  while(!glfwWindowShouldClose(window)) {
    renderer->render();
    handleEscape(window);
    handleControls(window, camera);
    glfwSwapBuffers(window);
    glfwPollEvents();
  }
}

void mouseCallback (GLFWwindow* window, double xpos, double ypos) {
  Renderer* renderer = (Renderer*) glfwGetWindowUserPointer(window);
  renderer->getCamera()->handleRotateForce(window, xpos, ypos);
}

int main() {
  testZmq();
  GLFWwindow* window = init();
  glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
  Camera* camera = new Camera();
  World* world = new World();
  Renderer* renderer = new Renderer(camera, world);
  world->attachRenderer(renderer);
  world->addCube(glm::vec3(0, 10, 0));
  glfwSetWindowUserPointer(window, (void*)renderer);
  glfwSetCursorPosCallback(window, mouseCallback);
  if(window == NULL) {
    return -1;
  }
  loop(window, renderer, camera);
  glfwTerminate();
  delete renderer;
  delete world;
  delete camera;
  return 0;
}
