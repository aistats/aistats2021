csv_file_path = "Poster_session.csv"
html_template_path = "sample_posters_session_file.html"

def load_csv(csv_file_path):
    with open(csv_file_path, "r") as csv_loader:
        lines = csv_loader.readlines()

    poster_dict = dict()
    current_poster_session = 0
    empty = False
    for line in lines:
        chunks = line.split("\t")
        chunks = [item for item in chunks if item!=""]
        if len(chunks) < 4:
            if not empty:
                current_poster_session += 1
                poster_dict[current_poster_session] = []
                empty = True
        else:
            poster_num, paper_id, paper_name, author = chunks
            poster_dict[current_poster_session].append([poster_num, paper_id, paper_name, author])
            empty = False

    return poster_dict


def generate_posters_session_page(csv_file_path, html_template_file_path):
    with open(html_template_file_path, "r") as html_loader:
        text = html_loader.readlines()

    posters_dict = load_csv(csv_file_path)
    table_posters_lines = []

    for key in posters_dict.keys():
        header_text = "<h2><span id={}>Poster Session {} (April 9)</span></h2>".format("Poster_Session{}".format(key), key)
        table_posters_lines.append(header_text)
        for item in posters_dict[key]:
            poster_num, paper_id, paper_name, author = item
            author_surname, author_name = author.split(",")
            table_posters_lines.append("<p>Poster {}: <b>{}</b><br>{} {}</p>".format(poster_num, paper_name, author_name, author_surname))

    html_output = []

    for line in text:
        if "{contents}" not in line:
            html_output.append(line)
        else:
            html_output.extend(table_posters_lines)
    with open("poster_sessions.html", "w") as html_writer:
        html_writer.writelines(html_output)


generate_posters_session_page(csv_file_path=csv_file_path, html_template_file_path=html_template_path)


