# This file is part of pdf-convertor.
#
# pdf-convertor is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pdf-convertor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pdf-convertor. If not, see <https://www.gnu.org/licenses/>.

import re


def titlu_unitate(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if i < n-3:
            if (text_attributes_list[i][0] == 'UNITATEA' and text_attributes_list[i][1] == 13.549758911132812
                    and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO'
                    and 63.043701171875 <= text_attributes_list[i+1][1] <= 64.3302993774414
                    and text_attributes_list[i+1][2] == 'ITCKabelStd-UltraRO' and 20 <= text_attributes_list[i+2][1] == 23.0
                    and text_attributes_list[i+2][2] == 'ITCKabelStd-BoldRO'):
                # Combine text for titlu unitate
                html = f"""
                <div class="center">
                    <h1 class="titlu-unitate">
                        <span class="text-unitate">UNITATEA<br/><span class="numar-unitate">{text_attributes_list[i+1][0]}</span></span>
                    {text_attributes_list[i+2][0]}
                    </h1>
                </div>
                <p class="clear"></p>\n
                """
                new_text_attributes_list.append([html, 100, '100', 100, (1, 0, 0)])
                i += 3
            else:
                new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list


def ol_li(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][1] == 10.779999732971191 or text_attributes_list[i][1] == 11.384419441223145:
            result = re.split(r'\s(?=[a-z]\))', text_attributes_list[i][0])
            if len(result) == 1:
                new_text_attributes_list.append(text_attributes_list[i])
            else:
                list_items_html = f'''
                        <ol class="lower_alpha">
                '''
                for k in range(1, len(result)):
                    list_items_html += f'''
                            <li>{result[k][2:]}</li>
                '''
                list_items_html += f'''
                        </ol>
                '''
                new_text_attributes_list.append([result[0]+list_items_html, text_attributes_list[i][1],
                                                 text_attributes_list[i][2], text_attributes_list[i][3],
                                                 text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 11.5:
            result = re.split(r'\s(?=[a-z]\))', text_attributes_list[i][0])
            if len(result) == 1:
                new_text_attributes_list.append(text_attributes_list[i])
            else:
                list_items_html = f'''
                        <ol class="lower_alpha">
                '''
                for k in range(0, len(result)):
                    list_items_html += f'''
                            <li>{result[k][2:]}</li>
                '''
                list_items_html += f'''
                        </ol>
                '''
                new_text_attributes_list.append([list_items_html, text_attributes_list[i][1],
                                                 text_attributes_list[i][2], text_attributes_list[i][3],
                                                 text_attributes_list[i][4]])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list


def bkgr_read(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if (text_attributes_list[i][1] == 11.5 and text_attributes_list[i][2] == 'MinionPro-Regular'
                and text_attributes_list[i][4][0] == 255 and text_attributes_list[i][4][1] == 253
                and 232 <= text_attributes_list[i][4][2] <= 233):
            # bkgr_read
            html = f"""
            <div class="bkgr-read">
                    <p>{text_attributes_list[i][0]}</p>
                </div>\n
                """
            new_text_attributes_list.append([html, 103, '103', 103, (1, 0, 3)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def bkgr_pers(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][1] == 10.779999732971191 and text_attributes_list[i][2] == 'PTSans-Regular' and text_attributes_list[i][4] == (11, 11, 11):
            # bkgr_pers
            html = f"""
                <div class="bkgr-pers">
                        <p>{text_attributes_list[i][0]}</p>
                    </div>\n
                    """
            new_text_attributes_list.append([html, 104, '104', 104, (1, 0, 4)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def text_imp(text_attributes_list):
    new_text_attributes_list = []

    i = 0
    while i < len(text_attributes_list):
        if text_attributes_list[i][0].strip() == 'Important':
            html = f"""
            <h3 class="important">Important</h3>
            """

            new_text_attributes_list.append([html, 109, '109', 109, (1, 0, 9)])
            i += 1
        elif text_attributes_list[i][4] == (1, 0, 8):
            html = f"""
            <div class="bkgr-imp">
            {text_attributes_list[i][0]}
            </div>
            """
            new_text_attributes_list.append([html, 108, '108', 108, (1, 0, 8)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list


def text_galben(text_attributes_list):
    new_text_attributes_list = []
    i = 1
    k = 0
    if (254 <= text_attributes_list[0][4][0] <= 254 and text_attributes_list[0][4][1] == 243
            and 231 <= text_attributes_list[0][4][2] <= 229):
        html_galben = text_attributes_list[0][0]
    else:
        html_galben = ""
        new_text_attributes_list = [text_attributes_list[0]]

    while i < len(text_attributes_list):
        if (text_attributes_list[i][4][0] == 254 and text_attributes_list[i][4][1] == 243
                and text_attributes_list[i][4][2] == 229):
            html_galben += text_attributes_list[i][0]
            i += 1
        elif (text_attributes_list[i][4][0] != 254 and text_attributes_list[i][4][1] != 243
              and text_attributes_list[i][4][2] != 229 and text_attributes_list[i-1][4][0] == 254
              and text_attributes_list[i-1][4][1] == 243
              and text_attributes_list[i-1][4][2] == 229) or (text_attributes_list[i] == text_attributes_list[-1]):

            html_galben = f"""
            <div class="bkgr-yellow">
            <p>{html_galben}</p>
            </div>
            """
            if html_galben != f"""
            <div class="bkgr-yellow">
            <p></p>
            </div>
            """:
                new_text_attributes_list.append([html_galben, 109, '109', 109, (1, 0, 9)])

            new_text_attributes_list.append(text_attributes_list[i])
            html_galben = ""
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def paragraph(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][1] == 11.5 and text_attributes_list[i][2] == 'MinionPro-Regular' and text_attributes_list[i][4] == (255, 255, 255):
            # paragraph
            html = f"""
            <p>{text_attributes_list[i][0]}</p>
            """
            new_text_attributes_list.append([html, 111, '111', 111, (1, 1, 1)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list
