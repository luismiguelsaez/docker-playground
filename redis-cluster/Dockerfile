FROM ruby:3

RUN gem install redis -v 3.3.0

RUN curl https://raw.githubusercontent.com/zvelo/redis-trib/master/redis-trib.rb -o /usr/local/bin/redis-trib.rb \
    && chmod +x /usr/local/bin/redis-trib.rb

ENTRYPOINT ["/usr/local/bin/redis-trib.rb"]
