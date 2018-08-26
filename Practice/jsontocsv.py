#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import sys
import codecs     

json_path = sys.argv[1]
csv_path = sys.argv[2]

def JsontoCSV():
    with codecs.open(json_path,'r',encoding='utf-8') as data_file:
        x = json.loads(data_file.read())
        with codecs.open(csv_path,"w", newline='', encoding='utf-8') as csvfile:
            f = csv.writer(csvfile, delimiter='\t', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
            # 表头
            # f.writerow(["derivation", "example", "explanation", "pinyin", "word", "abbreviation"])
            f.writerow([str(k) for k,v in x[0].items()])
            for x in x :
                # f.writerow([
                #     str(x["derivation"]), str(x["example"]), 
                #     str(x["explanation"]), str(x["pinyin"]), 
                #     str(x["word"]), str(x["abbreviation"])
                #     ])
                f.writerow(["\'" + str(v) + "\'" for k,v in x.items()])

if __name__ == "__main__":
    JsontoCSV()
    # secure-file-priv参数是用来限制LOAD DATA, SELECT ... OUTFILE, and LOAD_FILE()传到哪个指定目录的。

    # - ure_file_priv的值为null ，表示限制mysqld 不允许导入|导出
    # - 当secure_file_priv的值为/tmp/ ，表示限制mysqld 的导入|导出只能发生在/tmp/目录下
    # - 当secure_file_priv的值没有具体值时，表示不对mysqld 的导入|导出做限制

    # 1. 查找secure-file-priv(指定导入/导出文件夹)
    # ```sql
    # show variables like '%secure%';

    # secure_file_priv ===>> /var/lib/mysql-files/
    # ```

    # Linux： 修改/etc/my.cnf 添加 [mysqld] secure_file_priv =  

    # 2. 将要导入的文件放到该文件夹下
    # ```sql
    # -- 导出
    # select * from ci_table
    # into outfile '/var/lib/mysql-files/ci.csv'
    # fields terminated by ','
    # optionally enclosed by '"'
    # lines terminated by '\n';

    # -- 导入
    # load data infile '/var/lib/mysql-files/word.csv'
    # into table word
    # fields terminated by '\t'
    # optionally enclosed by "'"
    # lines terminated by '\r\n'
    # ignore 1 lines (word,oldword,strokes,pinyin,radicals,explanation,more);
    # ```
    # ignore 1 ... #忽略第一行标题行 需要导入的列展示出来
    # word,oldword,strokes,pinyin,radicals,explanation,more