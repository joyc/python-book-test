#!/bin/sh
################################################################################
# SCRIPT NAME        : file_sync.sh
# SCRIPT DESCRIPTION : ファイル用バックアップ&同期スクリプト
# OPTION             : N/A
# ARGUMENT           : $1 = 何でも可
# RETURN             : 0       :       正常終了
#                    : 1       :       引数異常
################################################################################
# Ver. When        Who               Description
# 1.0  2018/06/04  ACN tanaka         初回リリース
################################################################################ 

# 設定読み込み
. ./alaya_conf.sh

# Begin file sync to DR server.
sudo echo `date '+%Y/%m/%d %H:%M:%S'`" [Start] Sync files to DR server" >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?


# automake by pyshell 
# start ---->


sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

sudo rsync -ahvO --delete -e "$SSH_CMD" --inplace /bk/alaya$ALAYA_BAR_DIR/template/ alaya@$IP_ADDRESS:$ALAYA_BAR_DIR/template >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
echo `date '+%Y/%m/%d %H:%M:%S'`" "/alaya/customer/mhlw_roudoukyoku/template" has been synced." >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?


# <---- end
# automake by pyshell 


# Closing file sync to DR server.
sudo echo `date '+%Y/%m/%d %H:%M:%S'`" [End] Sync files to DR server" >> $APP_LOG_DIR/alaya_file_sync.$VAR_DATE.log
check_error $?

logger [Not_Notify] ${0#*/} 正常終了
check_error $?
exit 0
