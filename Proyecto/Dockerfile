FROM openjdk:17.0.2-jdk
VOLUME /tmp
EXPOSE 8080
ADD src/main/resources/static/proyectogtics-2c0efe2dc630.json /tmp/clavegcs.json
ADD ./target/Proyecto-0.0.1-SNAPSHOT.jar springlezz.jar
ENTRYPOINT ["java", "-jar","springlezz.jar"]