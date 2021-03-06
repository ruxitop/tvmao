#!/usr/bin/python

# coding: utf-8



import os

import tvmao


link = "https://www.tvmao.com"


#CCTV5-PLUS"5+"   CCTV11“戏曲”  CCTV12“法制“ CCTV13“新闻” CCTV15“少儿” CCTV16“音乐”

CCTV_prog = ['CCTV1', 'CCTV2', 'CCTV3', 'CCTV4', 'CCTV5', 'CCTV6','CCTV7','CCTV8','CCTV9','CCTV10','CCTV11','CCTV12','CCTV13','CCTV15','CCTV16','CCTV5-PLUS']
epg_path = 'epg/CCTV/';


if not os.path.exists(epg_path):
	os.makedirs(epg_path)


for prog in CCTV_prog:
	epg_name = epg_path+prog+'.txt';
	with open(epg_name, "w+") as f:
		f.write("")
	f.close()

	for num in range(1, 8):
		sublink = "/program/CCTV-"+prog+"-w"+str(num)+".html";
		tvmao.get_program(link, sublink, num, epg_name);


#BTV10"卡酷" HLJ"黑龙江" HUNANTV2"金鹰卡通" TJTV“天津”

province_prog = ['AHTV1', 'BTV1', 'BTV10', 'CCQTV1', 'FJTV2', 'GDTV1', 'SZTV1',  'GUIZOUTV1', 'HLJTV1','HNTV1','HUBEI1','HUNANTV1','HUNANTV2','JSTV1','JXTV1','LNTV1','SDTV1','DONGFANG1','SCTV1','TJTV1','ZJTV1' ]	

epg_path = 'epg/WeiShi/';

if not os.path.exists(epg_path):
	os.makedirs(epg_path)
for prog in province_prog:
	epg_name = epg_path+prog+'.txt';
	with open(epg_name, "w+") as f:
		f.write("")
	f.close()

	print(prog)

	for num in range(1, 8):
		sublink = "/program_satellite/"+prog+"-w"+str(num)+".html";
		tvmao.get_program(link, sublink,num,epg_name);


#付费节目 CCTVPAYFEE4"风云剧场" CCTVPAYFEE5"世界地理" cctvPAYFEE7"怀旧剧场" CCTVPAYFEE20"梨园" SITV13"卫生健康" BAMC4"四海钓鱼" GLOBALGO"环球购物" CCTVFXZL"发现之旅"

province_prog = ['CCTVPAYFEE4', 'CCTVPAYFEE5', 'CCTVPAYFEE7', 'CCTVPAYFEE20','SITV13','BAMC4','GLOBALGO','CCTVFXZL' ]

epg_path = 'epg/SZFF/';

if not os.path.exists(epg_path):
        os.makedirs(epg_path)
for prog in province_prog:
        epg_name = epg_path+prog+'.txt';
        with open(epg_name, "w+") as f:
                f.write("")
        f.close()

        print(prog)

        for num in range(1, 8):
                sublink = "/program_digital/"+prog+"-w"+str(num)+".html";
                tvmao.get_program(link, sublink, num, epg_name);





#境外节目 HNTV2"都市" HNTV3"民生" HNTV4"政法" HNTV5"电视剧" HNTV6"新闻" HNTV8"公共" HNTV9'新农村' HNXCTV1'许昌综合' HNXCTV2'许昌公共'

province_prog = ['HNTV2','HNTV3','HNTV4','HNTV5','HNTV6','HNTV8','HNTV9','HNXCTV1','HNXCTV2' ]



epg_path = 'epg/HN-BenDi/';

if not os.path.exists(epg_path):

        os.makedirs(epg_path)

for prog in province_prog:

        epg_name = epg_path+prog+'.txt';

        with open(epg_name, "w+") as f:

                f.write("")

        f.close()

        print(prog)

        for num in range(1, 8):

                sublink = "/program/HNTV-"+prog+"-w"+str(num)+".html";

                tvmao.get_program(link,sublink,num,epg_name);



#境外节目 凤凰卫视 凤凰资讯

province_prog = ['PHOENIX-PHOENIX1','PHOENIX-INFONEWS' ]



epg_path = 'epg/JingWai/';

if not os.path.exists(epg_path):

        os.makedirs(epg_path)

for prog in province_prog:

        epg_name = epg_path+prog+'.txt';

        with open(epg_name, "w+") as f:

                f.write("")

        f.close()

        print(prog)

        for num in range(1, 8):

                sublink = "/program/PHOENIX-"+prog+"-w"+str(num)+".html";

                tvmao.get_program(link, sublink, num, epg_name);





#境外节目 XINGKONG1"星空"

province_prog = ['XINGKONG1' ]



epg_path = 'epg/JingWai/';

if not os.path.exists(epg_path):

        os.makedirs(epg_path)

for prog in province_prog:

        epg_name = epg_path+prog+'.txt';

        with open(epg_name, "w+") as f:

                f.write("")

        f.close()

        print(prog)

        for num in range(1, 8):

                sublink = "/program/STARTV-"+prog+"-w"+str(num)+".html";

                tvmao.get_program(link, sublink, num, epg_name);





#家有购物

province_prog = ['JIAYOUGO' ]



epg_path = 'epg/SZFF/';

if not os.path.exists(epg_path):

        os.makedirs(epg_path)

for prog in province_prog:

        epg_name = epg_path+prog+'.txt';

        with open(epg_name, "w+") as f:

                f.write("")

        f.close()

        print(prog)

        for num in range(1, 8):

                sublink = "/program/LZCATV-"+prog+"-w"+str(num)+".html";

                tvmao.get_program(link, sublink, num, epg_name);





#家家购物



province_prog = ['JIAJIAMALL' ]



epg_path = 'epg/SZFF/';

if not os.path.exists(epg_path):

        os.makedirs(epg_path)

for prog in province_prog:

        epg_name = epg_path+prog+'.txt';

        with open(epg_name, "w+") as f:

                f.write("")

        f.close()

        print(prog)

        for num in range(1, 8):

                sublink = "/program/TJCATV-"+prog+"-w"+str(num)+".html";

                tvmao.get_program(link, sublink, num, epg_name);
                print(epg_path)
