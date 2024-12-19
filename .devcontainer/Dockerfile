FROM ubuntu:22.04

# LABEL maintainer="Kota Isayama"

ARG username=vscode
ARG useruid=1000
ARG usergid=${useruid}

RUN apt update && \
  apt install -y --no-install-recommends \
  curl \
  git \
  wget \
  openssh-client \
  sudo &&\
# create user
  groupadd --gid ${useruid} ${username} && \
  useradd -s /bin/bash --uid ${useruid} --gid ${usergid} -m ${username} && \
  echo ${username} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${username} && \
  chmod  0440 /etc/sudoers.d/${username} && \
# install Python3.11
   apt install -y --no-install-recommends python3 python3-pip
