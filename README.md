# Realtime Stock Market Sentiment Analysis 
Realtime Sentiment Analysis on Stock Data from Twitter Streams


### Environment Variables

Add the following environment variables to your bash profile


    export ALPACA_API_KEY=""
    export ALPACA_SECRET_KEY=""

    export TWITTER_API_KEY=""
    export TWITTER_API_SECRET=""
    export TWITTER_ACCESS_TOKEN=""
    export TWITTER_ACCESS_TOKEN_SECRET=""
    export TWITTER_BEARER_TOKEN=""


### How to start program
Step 1: Run Zookeeper

    cd ~
    cd ProgramFiles/kafka/kafka_2.13-2.8.0
    bin/zookeeper-server-start.sh config/zookeeper.properties

Step 2: Start Kafka Server
    
    cd ~
    cd ProgramFiles/kafka/kafka_2.13-2.8.0
    bin/kafka-server-start.sh config/server.properties

Step 3: Create Topics if not created already

    kafka-topics.sh --bootstrap-server localhost:9092 --topic topic-twitter-response --create --partitions 3 --replication-factor 1

    kafka-topics.sh --bootstrap-server localhost:9092 --topic topic-twitter-hashtags --create --partitions 3 --replication-factor 1