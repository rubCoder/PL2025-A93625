import sys
import re

def convert_headers(line):
    match = re.match(r'^(#{1,6})\s+(.*)', line.strip())  # Remove espaços extras no início e fim
    if match:
        level = len(match.group(1))  # Conta quantos '#' existem
        return f"<h{level}>{match.group(2).strip()}</h{level}>"  # Remove espaços extras do título
    return line  # Retorna a linha original se não for cabeçalho


def convert_bold_italic(line):
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)  # **bold**
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)      # *italic*
    return line

def convert_links(line):
    return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

def convert_images(line):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

def convert_ordered_list(md_text):
    lines = md_text.split('\n')
    html_lines = []
    in_list = False
    
    for line in lines:
        match = re.match(r'^(\d+)\.\s+(.*)', line)
        if match:
            if not in_list:
                html_lines.append("<ol>")
                in_list = True
            html_lines.append(f"<li>{match.group(2)}</li>")
        else:
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append(line)
    
    if in_list:
        html_lines.append("</ol>")
    
    return '\n'.join(html_lines)

def markdown_to_html(md_text):
    md_text = convert_ordered_list(md_text)
    html_lines = []
    
    for line in md_text.split("\n"):
        line = convert_headers(line)
        line = convert_bold_italic(line)
        line = convert_links(line)
        line = convert_images(line)
        html_lines.append(line)
    
    return "<br>".join(html_lines)


def main():
   
    md_text = []  
    
    for linha in sys.stdin:
        linha = linha.strip()
        if linha == "END":  
            break  
        md_text.append(linha)  
    
    markdown_input = "\n".join(md_text)
    
    # Converte o Markdown para HTML
    html_output = markdown_to_html(markdown_input)

  
    print(html_output)
        
if __name__ == "__main__":
    main()