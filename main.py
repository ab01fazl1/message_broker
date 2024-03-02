from queue import Queue

# a message class -> topic, content, acknowledged or seen
class Message:
    def __init__(self, content, seen=False):
        self.content = content
        self.seen = seen

    def __str__(self) -> str:
        return self.content
    
    def see(self):
        self.seen = True

class Topic:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
class Publisher:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    # publish a message to a topic 
    def publish(self, message: Message, topic: Topic):
        topics.setdefault(topic, Queue()).put(message)

class Subscriber:
    def __init__(self, name):
        self.name = name
        self.subscribed_topics = []
    
    def __str__(self) -> str:
        return self.name
    
    # subscribe to a topic
    def subscribe(self, topic: Topic):
        if topic not in self.subscribed_topics:
            self.subscribed_topics.append(topic)
    
    # read the messages
    def consume(self):
        # go through subbed messages
        for topic in self.subscribed_topics:
            # get topic Q
            topic_q = topics.get(topic)
            # read messages one by one
            for q in range(topic_q.qsize()):
                message = topic_q.get()
                print(message)
                message.see()

# map a topic objects to a queue object
topics = {}

p1 = Publisher(name='a')
print(p1)

s1 = Subscriber(name='s')
print(s1)

t1 = Topic(name='news')
print(t1)

s1.subscribe(topic=t1)
print('subscribed')

m1 = Message(content='bad news')
print(m1)

p1.publish(message=m1,topic=t1)
print('published')

print(topics)

s1.consume()
print('consumed')