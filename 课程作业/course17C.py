import os
import gradio as gr
import webbrowser

def initialization():
    dict = {}

    if os.path.exists('dict.txt'):
        with open('dict.txt', 'r', encoding='utf-8') as f:
            source = f.read()
            lines = source.split('\n')
            for line in lines[:-1]:
                en = line.split(':')[0]
                cn = line.split(':')[1].split(',')
                dict[en] = cn
    else:
        pass

    f.close()
    return dict


def add_word(en, cn):
    dict = initialization()
    if en in dict:
        if cn in dict[en]:
            return gr.Markdown.update(value="添加失败，该单词释义已存在", visible=True)
        else:
            outputs = ''
            dict[en].append(cn)
            print(dict)
            with open('dict.txt', 'w', encoding='utf-8') as f:
                for word in list(dict.keys()):
                    outputs += ('{}:{}\n'.format(word, ','.join(dict[word])))
                f.write(outputs)
    else:
        with open('dict.txt', 'a', encoding='utf-8') as f:
            f.write('{}:{}\n'.format(en, cn))

    f.close()
    return gr.Markdown.update(value="添加成功", visible=True)


def search_word(word):
    dict = initialization()
    if word in dict:
        return gr.Textbox.update(value=','.join(dict.get(word)), visible=True)
    else:
        return gr.Textbox.update(value="词典中未找到该单词", visible=True)


def delete_word(word):
    dict = initialization()
    for w in word:
        dict.pop(w, None)
    with open('dict.txt', 'w', encoding='utf-8') as f:
        for word in dict:
            f.write('{}:{}\n'.format(word, ','.join(dict[word])))

    return gr.update(choices=list(dict.keys()), label="词库")


def update_when_select_tab():
    dict = initialization()
    return gr.CheckboxGroup.update(choices=list(dict.keys()))


dict = initialization()
LIBRARIES = list(dict.keys())


with gr.Blocks(title="字典程序") as webui:
    with gr.Tabs():
        with gr.TabItem("添加单词"):
            fn = add_word
            with gr.Row():
                with gr.Column():
                    inputs_en = gr.Textbox(label="输入要添加的单词")
                    inputs_cn = gr.Textbox(label="输入单词释义")
                    search_btn = gr.Button("添加")
                with gr.Column():
                    examples = gr.Examples(label="词库", examples=list(dict.keys()), inputs=gr.Textbox(visible=False), examples_per_page='50')
            outputs = gr.Markdown(visible=False)
            search_btn.click(fn=fn, inputs=[inputs_en, inputs_cn], outputs=outputs)

        with gr.TabItem("搜索单词"):
            fn = search_word
            with gr.Row():
                with gr.Column():
                    inputs = gr.Textbox(label="输入要搜索的单词")
                    outputs = gr.Textbox(label="单词释义", visible=False)
                    search_btn = gr.Button("搜索")
                with gr.Column():
                    examples = gr.Examples(label="词库", examples=list(dict.keys()), inputs=gr.Textbox(visible=False), examples_per_page='50')
            search_btn.click(fn=fn, inputs=inputs, outputs=outputs)

        with gr.Tab("删除单词") as delete_word_tab:
            fn = delete_word
            inputs = gr.CheckboxGroup(choices=list(dict.keys()), label="词库")
            delete_btn = gr.Button("删除")
            delete_word_tab.select(fn=update_when_select_tab, inputs=None, outputs=inputs)
            delete_btn.click(fn=fn, inputs=inputs, outputs=inputs)

    with gr.Row():
        description = gr.Markdown(value="<center>Homework of Computer & Network Course 17, By Akiko, 221112013</center>")


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:7860')
    webui.launch(share=True)
