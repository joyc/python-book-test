#!/bin/sh
################################################################################
# SCRIPT NAME        : alaya_conf.sh
# SCRIPT DESCRIPTION : 設定ファイル
#                    : 各種パス等の変数はここへ記載する
# OPTION             : N/A
# ARGUMENT           : 
# RETURN             : 
#                    : 
################################################################################
# Ver. When        Who               Description
# 1.0  2016/11/22  ACN xxxxx         初回リリース
################################################################################

# Set common constants
VAR_DATE=`date '+%F'`
APP_LOG_DIR="/bk/alaya/logs"

#  Set constants for file_backup_sync.sh
readonly ALAYA_DIR="/app/cms"
readonly BK_ALAYA_DIR="/bk/alaya/app/cms"

#  Set constants for files_sync.sh
readonly ALAYA_DIR_TOMCAT="/app/cms/tomcat/webapps/ROOT"
readonly ALAYA_BAR_DIR="/app/cms/alaya/customer/mhlw_kourou"
readonly IP_ADDRESS="172.17.22.48"
readonly SSH_CMD="ssh -i /home/hcmsroujobservices01/.ssh/id_rsa"

#  Set common function
check_error() {
	if [ $1 -ne 0 ];then
		logger [Job_Abended] ${0#*/} 異常終了
		exit 1
	fi
}