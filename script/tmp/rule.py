# -*- coding: utf-8 -*-

rule = {
    u"互联网": [u"IT", u"刘兴亮", u"守兔网", u"李辉steven", u"互联网思维", u"产品经理", u"程序员", u"程序猿", u"编程",
                u"码农", u"交互设计", u"UI设计"],
    # u"情感/心理": [u"夫妻", u"婚恋", u"多愁善感", u"婚姻", u"爱情", u"情爱", u"心灵语录", u"情窦初开", u"心灵鸡汤", u"治愈",
    #            u"两性", u"情感咨询", u"情感加油站", u"心理咨询", u"心理辅导"],
    # u"游戏/漫画": [u"游戏", u"织画", u"漫画", u"西洋画", u"LOL", u"招贴画", u"电竞", u"棋画", u"英雄联盟", u"板画", u"动漫",
    #            u"策画", u"网游", u"二次元", u"静物画", u"手游", u"连环画", u"电玩", u"玩家", u"游戏机", u"页游", u"单机游",
    #            u"宅基腐", u"cos", u"dota", u"部落冲突", u"水墨画", u"魔兽", u"星际争霸", u"火影", u"海贼王"],
    # u"教育/培训": [u"学校", u"考试", u"学习资料", u"军训", u"课堂", u"小学", u"留学", u"中学", u"研究生", u"初中", u"博士",
    #            u"高中", u"本科", u"游学", u"幼教", u"幼儿园", u"学院", u"办学", u"校园", u"招生", u"集训", u"名师", u"名校",
    #            u"公开课"],
    # u"金融/保险": [u"金融", u"保险", u"投行", u"投资", u"私募", u"财经", u"股票", u"财富", u"寿险", u"基金", u"产险",
    #            u"个贷", u"融资", u"信用卡", u"p2p", u"期货", u"理财", u"券商", u"信托", u"人保", u"股市", u"投保", u"证券",
    #            u"黄金", u"银行", u"白银", u"股权", u"外汇", u"风投", u"创投", u"保费", u"汇兑"],
    # u"旅游": [u"旅游", u"旅客", u"导游", u"世界风光", u"旅会", u"之旅", u"旅资", u"攻旅食", u"旅居", u"驴友", u"环游",
    #         u"去哪玩", u"景点", u"各地美景", u"名胜", u"当地游", u"自由行", u"出境游", u"古典建筑", u"游记", u"自驾",
    #         u"沿途美景", u"背包客", u"入境游"],
    # u"美容": [u"美容", u"减肥", u"护肤", u"排毒", u"化妆", u"美妆", u"美丽攻略", u"养生", u"美发", u"整形", u"护发", u"调养",
    #         u"护理", u"养颜", u"瘦身", u"纹身", u"刺青", u"丰胸"],
    # u"科技/3C": [u"科技", u"3c", u"手机数码", u"智能设备", u"智能生活", u"电脑", u"可穿戴", u"VR", u"移动互联网", u"网络技术",
    #            u"手机", u"通讯", u"数码", u"云端", u"智能", u"终端", u"大数据技术", u"电脑技术", u"驱动", u"云技术",
    #            u"云计算", u"数字网络", u"技术研发", u"开发", u"高科", u"研究"],
    # u"食品/餐饮": [u"食品", u"餐桌", u"餐饮", u"用餐", u"私房菜", u"副食", u"茶", u"烘焙", u"食材", u"肉制品", u"零食",
    #            u"饮料", u"做饭", u"食谱", u"酒水", u"厨艺", u"菜谱", u"菜", u"中餐", u"西餐", u"果蔬", u"酒", u"鱼虾",
    #            u"烹饪", u"生鲜", u"菜肴", u"厨", u"烧饼", u"吃货", u"味蕾", u"调味", u"奶粉", u"炸鸡", u"水果", u"糕点",
    #            u"甜点", u"咖啡", u"酸奶", u"核桃", u"水饺", u"早餐", u"蛋糕", u"韩国料理", u"火锅", u"烤肉"],
    # u"服饰": [u"搭配", u"时装", u"穿衣", u"穿搭", u"鞋", u"帽", u"衣着", u"针织", u"服装搭配", u"穿衣搭配", u"时装", u"穿搭",
    #         u"穿衣", u"衣着搭配", u"男人穿衣", u"女性搭配", u"睡衣", u"内衣", u"休闲装", u"职业装", u"运动装", u"童装",
    #         u"服饰", u"衬衫", u"西装", u"布料", u"女装", u"男装", u"牛仔", u"洋装", u"工作服", u"丝绸", u"丝袜", u"原单",
    #         u"舞服", u"裤子", u"皮草" u"水貂" u"包包" u"家居服" u"手套" u"围巾" u"衣服" u"衣橱" u"婚纱"],
    # u"生活": [u"生活", u"天气", u"吃喝玩乐", u"潮生活", u"生活馆", u"同城", u"新鲜事", u"商场", u"公园", u"百货", u"物业",
    #         u"家居", u"俱乐部", u"格调", u"公益", u"新闻", u"家具", u"大小事", u"这些事", u"报纸", u"本地", u"卖场"],
    # u"运动/健身": [u"瑜伽", u"减肥", u"羽毛球", u"美体", u"健身", u"NBA", u"运动", u"篮球", u"足球", u"排球", u"体育",
    #            u"乒乓球", u"拳击", u"武术", u"橄榄球", u"网球", u"cba", u"跑步健身", u"竞走", u"马拉松", u"奥运会",
    #            u"世界杯", u"跳水", u"游泳", u"皮划艇", u"赛车", u"f1", u"赛马", u"马术", u"德甲", u"意甲", u"中超", u"恒大",
    #            u"申花", u"上港", u"英超", u"橄榄球", u"高尔夫", u"田径", u"台球", u"桌球", u"跆拳道", u"散打", u"皇马",
    #            u"巴萨", u"莱斯科特", u"科比", u"拜仁", u"c罗", u"梅西", u"库里", u"户外活动", u"俱乐部", u"摩托",
    #            u"体育用品", u"潜水", u"骑行", u"滑雪", u"击剑", u"体育"],
    # u"商务/电商": [u"电商", u"创业", u"企业家", u"销售", u"商业", u"商界", u"O2O模式", u"B2B模式", u"B2C模式", u"C2C模式",
    #            u"职场", u"创业企业家", u"商业模式", u"电子通讯", u"电子商务", u"电子商贸", u"导购平台", u"淘宝", u"微信营销",
    #            u"网络营销", u"微店"],
    # u"母婴/儿童": [u"育儿", u"养娃", u"亲子", u"儿童", u"怀胎", u"妊娠", u"孕妇", u"健康宝宝", u"婴儿", u"早教", u"奶粉"],
    # u"文化/艺术": [u"读书", u"电影", u"美剧", u"画画", u"文学社", u"雕塑学院", u"雕塑设计" u"书法" u"音乐", u"戏剧", u"戏曲",
    #            u"铜器", u"陶器", u"玉器", u"书画", u"钱币", u"油画", u"话剧", u"版画", u"艺术家", u"画家", u"鉴定家",
    #            u"收藏家", u"艺术家", u"艺术教育", u"工艺美术师", u"拍卖"],
    # u"法律": [u"劳动法", u"刑法", u"律师", u"法制", u"行政法规", u"司法", u"刑事责任", u"刑罚的法律"],
    # u"房地产/建筑": [u"房产", u"楼市", u"楼盘", u"建筑", u"不动产", u"地产", u"楼房", u"买房", u"房源", u"卖房", u"租房",
    #             u"别墅"],
    # u"汽车/交通": [u"汽车", u"交通广播", u"交通电台", u"auto", u"轮胎", u"车牌", u"车辆限行", u"交通快讯", u"交通运输",
    #            u"交规", u"驾驶", u"车险"],
    # u"娱乐八卦": [u"明星八卦", u"娱乐圈内幕", u"八卦猛料", u"明星囧事", u"娱乐新闻", u"花边新闻", u"娱乐圈", u"明星曝光",
    #           u"综艺报道", u"明星头条", u"娱乐花边新闻", u"八卦控", u"狗仔队", u"明星私生活", u"明星绯闻", u"八卦小道消息",
    #           u"韩娱八卦", u"圈内八卦", u"网络娱乐八卦"],
    # u"休闲娱乐": [u"休闲生活", u"休闲娱乐活动", u"琴棋书画", u"棋牌", u"麻将", u"扑克", u"垂钓", u"钓鱼", u"放风筝", u"曲艺",
    #           u"相声", u"脱口秀", u"魔术"],
    # u"媒体/杂志": [u"媒体单位", u"出版", u"杂志", u"杂志社", u"周刊", u"期刊", u"报刊", u"FM", u"广播", u"电视台", u"电台",
    #            u"晨报", u"报社", u"商报", u"日报", u"晚报", u"卫视", u"青年报", u"广告传媒"],
    # u"社会/民生": [u"社会民生", u"民生动态", u"百姓话题", u"民生焦点", u"廉租房", u"GDP", u"社保", u"就业", u"税收",
    #            u"民生新闻", u"社会热点", u"民声", u"民生事件"],
    # u"酒店/住宿": [u"酒店住宿", u"宾馆", u"旅馆", u"旅店", u"旅社", u"商旅", u"客店", u"客栈", u"经济型酒店", u"连锁酒店",
    #            u"公寓式酒店", u"商务型酒店", u"旅舍", u"民宿"],
    # u"医疗/健康": [u"医疗服务", u"健康管理", u"保健常识", u"中医养生", u"养生窍门", u"理疗", u"镭疗", u"放疗", u"治疗",
    #            u"电疗", u"浴疗", u"诊疗", u"化疗", u"蜡疗", u"食疗", u"营疗", u"磁疗", u"放射性同位素治疗", u"医疗体育",
    #            u"医疗器械", u"医生", u"医药", u"西医", u"医院", u"儿科", u"口腔"],
    # u"政务": [u"政务", u"政府部门", u"行政审批", u"政府服务", u"共青团动态", u"消防安全", u"公安局", u"警务资讯", u"税务局",
    #         u"财政部政委", u"政理", u"政论", u"政纲", u"政客", u"政要", u"政审", u"政绩", u"政坛", u"政策", u"政治犯",
    #         u"政局", u"政治指导员外务", u"侨务", u"派出所", u"警务站"],
    # u"家居": [u"家居风水", u"装修家居", u"家具设计", u"实木家具", u"室内装修", u"家具配置", u"智能家居", u"家居饰品",
    #         u"家居用品"]
}
