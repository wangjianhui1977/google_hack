from googlesearch import search  # 从googlesearch模块导入search函数，用于执行Google搜索
import time  # 导入time模块，用于添加延迟

def google_hack_search(query, max_results=100):
    # 使用Google Hacking语法进行搜索
    urls = []  # 初始化一个空列表，用于存储搜索结果的URL
    try:
        for url in search(query, num_results=max_results):  # 使用search函数执行搜索，尝试获取最多max_results个结果
            print(f"Found URL: {url}")  # 打印找到的URL
            urls.append(url)  # 将URL添加到列表中
            time.sleep(1)  # 等待1秒，避免频繁请求
            if len(urls) >= max_results:  # 如果已达到最大结果数，停止搜索
                break
    except Exception as e:
        print(f"An error occurred: {e}")  # 如果发生异常，打印错误信息
    return urls  # 返回收集到的URL列表

def save_results_to_file(urls, filename):
    # 将收集到的URL保存到文件中
    with open(filename, 'w', encoding='utf-8') as file:  # 打开指定的文件，以写入模式
        for url in urls:  # 遍历URL列表
            file.write(url + '\n')  # 将每个URL写入文件，并换行
    print(f"Results saved to {filename}")  # 打印保存成功的信息

if __name__ == "__main__":
    query = input("Enter your Google Hacking query: ")  # 提示用户输入Google Hacking查询
    filename = input("Enter the filename to save results: ")  # 提示用户输入保存结果的文件名
    urls = google_hack_search(query, max_results=100)  # 执行搜索，尝试获取最多100个结果
    save_results_to_file(urls, filename)  # 将结果保存到用户指定的文件中
