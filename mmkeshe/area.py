dictProvince = {2: '加密算法', 3: '加密算法', 4: '福建', 5: '甘肃', 6: '广东', 7: '广西', 8: '贵州', 9: '海南', 10: '河北',
                11: '河南', 12: '黑龙江', 13: '湖北', 14: '湖南', 15: '吉林', 16: '江苏', 17: '江西', 18: '辽宁',
                19: '内蒙古', 20: '宁夏', 21: '青海', 22: '山东', 23: '山西', 24: '陕西', 25: '上海', 26: '四川',
                27: '天津', 28: '西藏', 29: '新疆', 30: '云南', 31: '浙江', 32: '重庆', 33: '香港', 34: '澳门',
                35: '台湾'}

dictCity = {2: {52: '北京'}, 3: {36: '安庆', 37: '蚌埠', 38: '巢湖', 39: '池州', 40: '滁州', 41: '阜阳', 42: '淮北',
                               43: '淮南', 44: '黄山', 45: '六安', 46: '马鞍山', 47: '宿州', 48: '铜陵', 49: '芜湖', 50: '宣城',
                               51: '亳州',
                               3401: '合肥'}, 4: {53: '福州', 54: '龙岩', 55: '南平', 56: '宁德', 57: '莆田', 58: '泉州', 59: '三明',
                                                60: '厦门', 61: '漳州'},
            5: {62: '兰州', 63: '白银', 64: '定西', 65: '甘南', 66: '嘉峪关', 67: '金昌',
                68: '酒泉', 69: '临夏', 70: '陇南', 71: '平凉', 72: '庆阳', 73: '天水', 74: '武威', 75: '张掖'},
            6: {76: '广州', 77: '深圳', 78: '潮州', 79: '东莞', 80: '佛山', 81: '河源', 82: '惠州', 83: '江门',
                84: '揭阳', 85: '茂名', 86: '梅州', 87: '清远', 88: '汕头', 89: '汕尾', 90: '韶关', 91: '阳江',
                92: '云浮', 93: '湛江', 94: '肇庆', 95: '中山', 96: '珠海'}, 7: {97: '南宁', 98: '桂林', 99: '百色',
                                                                       100: '北海', 101: '崇左', 102: '防城港', 103: '贵港',
                                                                       104: '河池', 105: '贺州', 106: '来宾', 107: '柳州',
                                                                       108: '钦州', 109: '梧州', 110: '玉林'},
            8: {111: '贵阳', 112: '安顺', 113: '毕节', 114: '六盘水',
                115: '黔东南', 116: '黔南', 117: '黔西南', 118: '铜仁', 119: '遵义'}, 9: {120: '海口', 121: '三亚',
                                                                              122: '白沙', 123: '保亭', 124: '昌江',
                                                                              125: '澄迈县', 126: '定安县', 127: '东方',
                                                                              128: '乐东', 129: '临高县',
                                                                              130: '陵水', 131: '琼海', 132: '琼中',
                                                                              133: '屯昌县', 134: '万宁', 135: '文昌',
                                                                              136: '五指山', 137: '儋州'},
            10: {138: '石家庄', 139: '保定', 140: '沧州', 141: '承德', 142: '邯郸', 143: '衡水', 144: '廊坊', 145: '秦皇岛',
                 146: '唐山', 147: '邢台', 148: '张家口'}, 11: {149: '郑州', 150: '洛阳', 151: '开封', 152: '安阳', 153: '鹤壁',
                                                         154: '济源', 155: '焦作', 156: '南阳', 157: '平顶山', 158: '三门峡',
                                                         159: '商丘', 160: '新乡', 161: '信阳',
                                                         162: '许昌', 163: '周口', 164: '驻马店', 165: '漯河', 166: '濮阳'},
            12: {167: '哈尔滨', 168: '大庆',
                 169: '大兴安岭', 170: '鹤岗', 171: '黑河', 172: '鸡西', 173: '佳木斯', 174: '牡丹江', 175: '七台河',
                 176: '齐齐哈尔', 177: '双鸭山', 178: '绥化', 179: '伊春'}, 13: {180: '武汉', 181: '仙桃', 182: '鄂州',
                                                                      183: '黄冈', 184: '黄石', 185: '荆门', 186: '荆州',
                                                                      187: '潜江', 188: '神农架林区', 189: '十堰', 190: '随州',
                                                                      191: '天门', 192: '咸宁', 193: '襄樊', 194: '孝感',
                                                                      195: '宜昌', 196: '恩施'}, 14: {197: '长沙', 198: '张家界',
                                                                                                  199: '常德', 200: '郴州',
                                                                                                  201: '衡阳', 202: '怀化',
                                                                                                  203: '娄底', 204: '邵阳',
                                                                                                  205: '湘潭', 206: '湘西',
                                                                                                  207: '益阳', 208: '永州',
                                                                                                  209: '岳阳', 210: '株洲'},
            15: {211: '长春', 212: '吉林', 213: '白城', 214: '白山',
                 215: '辽源', 216: '四平', 217: '松原', 218: '通化', 219: '延边'}, 16: {220: '南京', 221: '苏州', 222: '无锡',
                                                                              223: '常州', 224: '淮安', 225: '连云港',
                                                                              226: '南通', 227: '宿迁', 228: '泰州',
                                                                              229: '徐州', 230: '盐城',
                                                                              231: '扬州', 232: '镇江'},
            17: {233: '南昌', 234: '抚州', 235: '赣州', 236: '吉安', 237: '景德镇', 238: '九江',
                 239: '萍乡', 240: '上饶', 241: '新余', 242: '宜春', 243: '鹰潭'}, 18: {244: '沈阳', 245: '大连', 246: '鞍山',
                                                                              247: '本溪', 248: '朝阳', 249: '丹东',
                                                                              250: '抚顺', 251: '阜新', 252: '葫芦岛',
                                                                              253: '锦州', 254: '辽阳',
                                                                              255: '盘锦', 256: '铁岭', 257: '营口'},
            19: {258: '呼和浩特', 259: '阿拉善盟', 260: '巴彦淖尔盟',
                 261: '包头', 262: '赤峰', 263: '鄂尔多斯', 264: '呼伦贝尔', 265: '通辽', 266: '乌海', 267: '乌兰察布市',
                 268: '锡林郭勒盟', 269: '兴安盟'}, 20: {270: '银川', 271: '固原', 272: '石嘴山', 273: '吴忠', 274: '中卫'},
            21: {275: '西宁', 276: '果洛', 277: '海北', 278: '海东', 279: '海南', 280: '海西', 281: '黄南', 282: '玉树'},
            22: {283: '济南', 284: '青岛', 285: '滨州', 286: '德州', 287: '东营', 288: '菏泽', 289: '济宁', 290: '莱芜',
                 291: '聊城', 292: '临沂', 293: '日照', 294: '泰安', 295: '威海', 296: '潍坊', 297: '烟台', 298: '枣庄',
                 299: '淄博'}, 23: {300: '太原', 301: '长治', 302: '大同', 303: '晋城', 304: '晋中', 305: '临汾', 306: '吕梁',
                                  307: '朔州', 308: '忻州', 309: '阳泉', 310: '运城'},
            24: {311: '西安', 312: '安康', 313: '宝鸡', 314: '汉中',
                 315: '商洛', 316: '铜川', 317: '渭南', 318: '咸阳', 319: '延安', 320: '榆林'}, 25: {321: '上海'}, 26: {322: '成都',
                                                                                                          323: '绵阳',
                                                                                                          324: '阿坝',
                                                                                                          325: '巴中',
                                                                                                          326: '达州',
                                                                                                          327: '德阳',
                                                                                                          328: '甘孜',
                                                                                                          329: '广安',
                                                                                                          330: '广元',
                                                                                                          331: '乐山',
                                                                                                          332: '凉山',
                                                                                                          333: '眉山',
                                                                                                          334: '南充',
                                                                                                          335: '内江',
                                                                                                          336: '攀枝花',
                                                                                                          337: '遂宁',
                                                                                                          338: '雅安',
                                                                                                          339: '宜宾',
                                                                                                          340: '资阳',
                                                                                                          341: '自贡',
                                                                                                          342: '泸州'},
            27: {343: '天津'}, 28: {344: '拉萨', 345: '阿里',
                                  346: '昌都', 347: '林芝', 348: '那曲', 349: '日喀则', 350: '山南'}, 29: {351: '乌鲁木齐', 352: '阿克苏',
                                                                                                353: '阿拉尔', 354: '巴音郭楞',
                                                                                                355: '博尔塔拉', 356: '昌吉',
                                                                                                357: '哈密', 358: '和田',
                                                                                                359: '喀什',
                                                                                                360: '克拉玛依',
                                                                                                361: '克孜勒苏', 362: '石河子',
                                                                                                363: '图木舒克', 364: '吐鲁番',
                                                                                                365: '五家渠', 366: '伊犁'},
            30: {367: '昆明', 368: '怒江', 369: '普洱', 370: '丽江', 371: '保山', 372: '楚雄', 373: '大理', 374: '德宏',
                 375: '迪庆', 376: '红河', 377: '临沧', 378: '曲靖', 379: '文山', 380: '西双版纳', 381: '玉溪', 382: '昭通'},
            31: {383: '杭州', 384: '湖州', 385: '嘉兴', 386: '金华', 387: '丽水', 388: '宁波', 389: '绍兴', 390: '台州',
                 391: '温州', 392: '舟山', 393: '衢州'}, 32: {394: '重庆'}, 33: {395: '香港'}, 34: {396: '澳门'}, 35: {397: '台湾'}}