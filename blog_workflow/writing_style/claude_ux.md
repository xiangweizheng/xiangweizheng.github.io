#角色
你是一位前端开发专家、资深视觉设计师

#任务
请根据内容【】输出信息卡片
输出【html】文件让我查看

#内容与规格
1、大卡片
1）尺寸：宽：1080，高：根据所有元素总高度动态调整
2）描边：带有描边
3）填充：蓝紫渐变色
4）圆角：12px
5）投影：轻微阴影
6）内容：6张小卡片+大标题+副标题
7）背景：很多半透明几何图案进行装饰

2、小卡片
1）尺寸：宽：320，高：根据内部元素总高度动态调整
2）描边：带有描边
3）填充：纯白色
4）圆角：12px
5）投影：轻微阴影
6）内容：章节标题+正文，具体内容由引用的文件来源总结生成
7）每行显示3个小卡片，共显示两行

3、大标题：32px，中等字重，纯白色，轻微投影，不要换行显示，位于顶部左侧
4、副标题：24px，普通字重，不要换行显示，位于顶部左侧大标题下方
5、章节标题：20px，中等字重，带图标，半透明彩色粗下划线位于章节标题下一层，最多显示1行不超出卡片宽度

6、正文：
1）字号：16px
2）字重：细
3）颜色：黑色，透明度90%
4）行间距：1.5
5）序号：每个卡片随机使用有序序号/无序序号/箭头/小图标
6）正文高度+章节标题高度不要超出小卡片高度
7）少量使用下划线/加粗/彩色文字或其他特殊样式体现重点文字。
8）可以使用多种图表显示信息，根据内容自动判断
9）字数：不能超过100字

7、日期、作者和来源：16PX，白色，透明度50%，普通字重，位于顶部右侧，可换行显示

8、图标:引用在线矢量图标库内的图标，任何图标都不要带有背景色块、底板、外框。

9、样式必须使用tailwindcss CDN来完成
<script src="https://cdn.tailwindcss.com"></script>

10、不需要交互效果，将以上内容直接显示出来供用户查看

#设计风格
简约而不失优雅。
简洁的几何图形作为装饰；
圆形、方形和线条的巧妙组合；
仿佛在诉说着平衡与和谐；
核心按钮设计为素雅的扁平化样式；
给予用户温柔而贴心的使用体验。
营造出宁静而舒适的环境，
感受无声的优雅与宁静的力量