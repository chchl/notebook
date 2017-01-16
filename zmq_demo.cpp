# include <zmq.h>
# include <stdio.h>
# include <unistd.h>
# include <string.h>

// server
int req_rep(){
    void *content = zmq_init(1);
    void *responser = zmq_socket(content, ZMQ_REP);
    zmq_bind(responser, "tcp://*:5555");
    while (1) {
        zmq_msg_t request;
        zmq_msg_init(&request,0);
        zmq_recv(responser, &request, 0);
        printf("received\n",);
        zmq_msg_close(&request);
        sleep(1);

        zmq_msg_t reply;
        zmq_msg_init_size(&reply, 5);
        memcpy(zmq_msg_data(&reply), "World", 5);
        zmq_send(responser, &reply, 0);
        zmq_msg_close(&reply);
    }
}
