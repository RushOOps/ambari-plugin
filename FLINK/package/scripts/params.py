#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import commands

# server configuration
config = Script.get_config()
cmd = "/usr/bin/hdp-select versions"
hdp_base_dir = '/usr/hdp/' + commands.getoutput(cmd)
flink_install_dir = hdp_base_dir + '/flink'

# params from flink-ambari-config
flink_download_url = config['configurations']['flink-ambari-config']['flink_download_uri']

hadoop_conf_dir = config['configurations']['flink-env']['hadoop_conf_dir']

# params from flink-conf.yaml
flink_yaml_content = config['configurations']['flink-env']['flink-conf.yaml']
flink_dependency_jar = config['configurations']['flink-env']['flink_dependency_jar']

# log4j
flink_log4j = config['configurations']['flink-env']['log4j.properties']

flink_user = "flink"
root = "root"