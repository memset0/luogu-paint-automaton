# Luogu Paint Automaton

洛谷冬日绘板脚本

前排广告，如果您有闲置的账号，可以把 cookies 给 **@ranwen** 帮助他绘制画板，他还可以帮您话您想要的图片哦 Orz.

### 工作原理

依次检查 todo 列表中的每个点是否和需要绘制的颜色向匹配，如果不是，就依次尝试用每个账号作图知道颜色被绘制成功

update1: 每次开始做时检查一遍，已经和目标颜色相同的点就不加入 todolist 里
update2: 不检查上色是否成功，只判断响应 json 的 status 

### 获取 cookies

洛谷验证登录状态需要 `__client_id` 和 `_uid` 。一般登录请求会发送 `__client_id` 到服务器，如果账号密码正确这个 `__client_id` 就可以获得登录状态。当然我们可以直接使用 `__client_id` 来获取登录状态，您只需要把 `__client_id` 放到脚本的对应位置即可。

需要注意的是，您可以通过删除 `__client_id` 并刷新来重置 `__client_id` 以登录下一个账号，而不是注销，否则登录状态会消失。

### 设置 todo

任务存在 `todo.list` 文件中，可以有任意多行，每行三个非负整数，分别是 x 坐标， y 坐标和颜色 c 。其中 x < 800 , y < 600 , c < 32 。

### 图片转换

~~先将图片转换为 ppm 格式，再用 https://github.com/quank123wip/ppmanalyzer 转化为 todo list .~~

咕咕咕
