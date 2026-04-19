from util import lines

# ========== 方法1：直接打开文件 ==========

print("=== 方法1：直接打开文件 ===")
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in lines(f):
        print(repr(line))  # repr() 显示换行符等不可见字符

# ========== 方法2：看看 blocks 怎么调用 lines ==========

print("\n=== 方法2：模拟 blocks 的调用过程 ===")


def my_blocks(file):
    """简化版 blocks，带打印，让你看清每一步"""
    block = []

    for line in lines(file):
        print(f"  lines() 产出: {repr(line)}")

        if line.strip():
            block.append(line)
            print(f"    → 加入当前块，block现在: {block}")
        elif block:
            result = ''.join(block).strip()
            print(f"    → 遇到空行，产出块: {repr(result)}")
            block = []
            print(f"    → 清空block")

    print(f"  循环结束，block剩余: {block}")


with open('input.txt', 'r', encoding='utf-8') as f:
    my_blocks(f)