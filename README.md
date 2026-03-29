第二次人工智能编程作业
1. 任务拆解与 AI 协作策略
在开发“学生信息与考场管理系统”时，我采取了“自底向上”的拆解策略，确保每个模块都符合教学大纲的工程规范：
 * 步骤 1：数据模型定义。首先要求 AI 构建 Student 类，重点在于利用 __init__ 初始化 5 个核心属性，并重写 __str__ 魔术方法，以便后续直接 print(obj) 时能输出整洁的中文信息。
 * 步骤 2：核心逻辑封装。要求 AI 将所有功能封装在 ExamSystem 类中。我指挥 AI 先实现文件读取逻辑（init_students），再依次开发查找、随机点名和文件生成功能。
 * 步骤 3：健壮性与合规性检查。在功能完成后，我要求 AI 增加 try-except 异常捕获块，并加入一个 staticmethod（静态方法）用于校验用户输入，以满足作业对技术规范的硬性要求。
 * 步骤 4：交互界面整合。最后编写 main() 函数，实现循环菜单，将所有功能串联成一个可运行的系统。
2. 核心 Prompt 迭代记录
 * 初代 Prompt： “用 Python 写一个学生管理系统，能读 txt 文件，能点名，能生成考场表。”
   * AI 生成的问题： 代码使用了 pandas 库（未讲授），且所有代码都堆在 main 函数里，没有体现面向对象编程（OOP）。
 * 优化后的 Prompt (追问)： “请重构代码。要求：
   * 必须使用 Student 和 ExamSystem 两个类。
   * 严禁使用 pandas，只能用 os, random, time 等标准库。
   * 必须包含一个静态方法校验数字输入。
   * 文件输出必须包含当前时间戳，且考场号要补零（如 01.txt）。”
3. Debug 与异常处理记录
 * 报错类型/漏洞现象： 在读取 人工智能编程语言学生名单.txt 时，程序因为文件中存在的空行导致 split('\t') 后的解包操作报错（ValueError: not enough values to unpack）。
 * 解决过程： 我通过观察代码发现，直接对每一行进行分割没有考虑到空行情况。我手动在 init_students 方法中增加了 if not line: continue 的逻辑判断，跳过空行，从而确保了数据解析的稳定性。此外，针对 random.sample 可能出现的采样数量超过总数的问题，我通过 check_number_input 静态方法进行了预先拦截。
4. 人工代码审查 (Code Review)
以下是我对 generate_admission_ticket 方法进行的逐行代码审查，证明我已完全掌握其逻辑：

def generate_admission_ticket(self, student_ids: List[str]):
    """生成准考证目录与文件：创建文件夹并在其内生成独立txt文件"""
    if not student_ids: return  # 防护性编程：如果学号列表为空则直接返回
    
    ticket_dir = "准考证"  # 定义目标文件夹名称
    try:
        # 调用 os 模块创建文件夹，exist_ok=True 表示如果文件夹已存在则不报错
        os.makedirs(ticket_dir, exist_ok=True) 
        
        # 遍历打乱后的学号列表，使用 enumerate 获取座位号（从1开始）
        for seat_num, id_num in enumerate(student_ids, 1):
            student = self.students[id_num] # 从字典中通过键（学号）获取学生对象
            
            # 使用 f-string 格式化文件名，:02d 表示将数字补零为2位（如 1 变为 01）
            file_name = f"{seat_num:02d}.txt" 
            file_path = os.path.join(ticket_dir, file_name) # 拼接完整的文件路径
            
            # 以写入模式打开文件，指定 utf-8 编码以支持中文
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"考场座位号：{seat_num}\n")
                f.write(f"姓名：{student.name}\n")
                f.write(f"学号：{student.id_num}\n")
        print(f"✅ 准考证文件生成成功！")
    except Exception as e:
        print(f"❌ 准考证生成失败：{str(e)}") # 捕获并提示可能的磁盘写入异常
