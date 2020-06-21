#!/usr/bin/env python3

# BGI script dumper

import glob
import os
import struct
import sys
import requests
import hashlib
import time
import json
import random
import bgi_common
import bgi_setup
import urllib.parse
import http.client
import random
import hashlib
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tmt.v20180321 import tmt_client, models 
 
def tencentcloudtar(q):
	cred = credential.Credential("AKIDYyGRV8NYJNIxKbv5YtynKbokUFm6nQjf", "f8ct0wugJpocHlvrix8fyaSKyPceVH5z") 
	httpProfile = HttpProfile()
	httpProfile.endpoint = "tmt.tencentcloudapi.com"

	clientProfile = ClientProfile()
	clientProfile.httpProfile = httpProfile
	client = tmt_client.TmtClient(cred, "ap-chongqing", clientProfile) 

	req = models.TextTranslateRequest()
	params = '{\"SourceText\":\"'+q+'\",\"Source\":\"auto\",\"Target\":\"zh\",\"ProjectId\":0}'
	req.from_json_string(params)
	resp = client.TextTranslate(req)
	data=json.loads(str(resp))
	print(data)
	
	print( data["TargetText"])
	return data["TargetText"]



def dump_text(fo, marker, id, text, comment):
	fo.write('//%s\n' % comment)
	fo.write('<%s%s%04d>%s\n' % (bgi_setup.slang,marker,id,text))
	# print(text)
	text = tencentcloudtar(text)
	time.sleep( 1 )
	
	for lang in bgi_setup.dlang:
		if bgi_setup.dcopy:
			fo.write('<%s%s%04d>%s\n' % (lang,marker,id,text))
		else:
			fo.write('<%s%s%04d>\n' % (lang,marker,id))
	fo.write('\n')
	
def dump_unique(fo, code_section, imarker):
	text_set = set()
	for addr in sorted(code_section):
		text, id, marker, comment = code_section[addr]
		if marker == imarker and text not in text_set:
			dump_text(fo, marker, id, bgi_common.escape(text), comment)
			text_set.add(text)

def dump_sequential(fo, code_section, imarker):
	for addr in sorted(code_section):
		text, id, marker, comment = code_section[addr]
		if marker == imarker:
			dump_text(fo, marker, id, bgi_common.escape(text), comment)
	
def dump_script(script):
	data = open(script, 'rb').read()
	hdr_bytes, code_bytes, text_bytes, config = bgi_common.split_data(data)
	text_section = bgi_common.get_text_section(text_bytes)
	code_section = bgi_common.get_code_section(code_bytes, text_section, config)
	fo = open(script+bgi_setup.dext, 'w', encoding=bgi_setup.denc)
	dump_unique(fo, code_section, 'N')        # names
	fo.write('///'+'='*80+'\n\n')
	dump_sequential(fo, code_section, 'T')    # text
	fo.write('///'+'='*80+'\n\n')
	dump_unique(fo, code_section, 'Z')        # other
	fo.close()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: bgi_dump.py <file(s)>')
		print('(only extension-less files amongst <file(s)> will be processed)')
		sys.exit(1)
	for arg in sys.argv[1:]:
		for script in glob.glob(arg):
			base, ext = os.path.splitext(script)
			if not ext and os.path.isfile(script):
				print('Dumping %s...' % script)
				dump_script(script)
			
