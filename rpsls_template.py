#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�᯵�ǰ
���ڣ�2019.11.25
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

comp_number=random.randrange(0,5)
player_choice_number=0
def name_to_number(name):
	if name == "ʯͷ" :
	    player_choice_number=0
	elif name == "ʷ����" :
	    player_choice_number=1
	elif name == "ֽ" :
		player_choice_number=2
	elif name == "����" :
		player_choice_number=3
	elif name == "����" :
		player_choice_number=4
	else:
		print("Error:No Correct Name")
  
"""
����Ϸ�����Ӧ����ͬ������
"""

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
	if number == 0:
		 comp_name="ʯͷ"
	elif number == 1:
		 comp_name="ʷ����"
	elif number == 2:
		 comp_name="ֽ"
	elif number == 3:
		 comp_name="����"
	elif number == 4:
		 comp_name="����"
"""
������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
"""

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice_number):
	if comp_number==player_choice_number:
		print("----------------")
		print("���ͼ��������һ����")
	elif comp_number == 3 and player_choice_number==0 :
		print("----------------")
		print("����ѡ��Ϊ:ʯͷ")
		print("�������ѡ��Ϊ:����")
		print("��Ӯ�ˣ�")
	elif comp_number==4 and player_choice_number==0 :
		print("----------------")
		print("����ѡ��Ϊ:ʯͷ")
		print("�������ѡ��Ϊ:����")
		print("��Ӯ�ˣ�")
	elif comp_number==1 and player_choice_number==0 :
		print("----------------")
		print("����ѡ��Ϊ:ʯͷ")
		print("�������ѡ��Ϊ:ʷ����")
		print("����Ӯ��")
	elif comp_number==2 and player_choice_number==0 :
		print("----------------")
		print("����ѡ��Ϊ:ʯͷ")
		print("�������ѡ��Ϊ:��")
		print("����Ӯ��")
	elif comp_number==2 and player_choice_number==1 :
		print("----------------")
		print("����ѡ��Ϊ:ʷ����")
		print("�������ѡ��Ϊ:��")
		print("����Ӯ��")
	elif comp_number==0 and player_choice_number==1 :
		print("----------------")
		print("����ѡ��Ϊ:ʷ����")
		print("�������ѡ��Ϊ:ʯͷ")
		print("��Ӯ�ˣ�")
	elif comp_number==3 and player_choice_number==1 :
		print("----------------")
		print("����ѡ��Ϊ:ʷ����")
		print("�������ѡ��Ϊ:����")
		print("����Ӯ��")
	elif comp_number==4 and player_choice_number==1 :
		print("----------------")
		print("����ѡ��Ϊ:ʷ����")
		print("�������ѡ��Ϊ:����")
		print("��Ӯ�ˣ�")
	elif comp_number==0 and player_choice_number==2 :
		print("----------------")
		print("����ѡ��Ϊ:��")
		print("�������ѡ��Ϊ:ʯͷ")
		print("��Ӯ�ˣ�")
	elif comp_number==1 and player_choice_number==2 :
		print("----------------")
		print("����ѡ��Ϊ:��")
		print("�������ѡ��Ϊ:ʷ����")
		print("��Ӯ�ˣ�")
	elif comp_number==3 and player_choice_number==2 :
		print("----------------")
		print("����ѡ��Ϊ:��")
		print("�������ѡ��Ϊ:����")
		print("����Ӯ��")
	elif comp_number==4 and player_choice_number==2 :
		print("----------------")
		print("����ѡ��Ϊ:��")
		print("�������ѡ��Ϊ:����")
		print("����Ӯ��")
	elif comp_number==0 and player_choice_number==3 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:ʯͷ")
		print("����Ӯ��")
	elif comp_number==1 and player_choice_number==3 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:ʷ����")
		print("��Ӯ�ˣ�")
	elif comp_number==2 and player_choice_number==3 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:��")
		print("��Ӯ�ˣ�")
	elif comp_number==4 and player_choice_number==3 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:����")
		print("����Ӯ��")
	elif comp_number==0 and player_choice_number==4 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:ʯͷ")
		print("����Ӯ��")
	elif comp_number==1 and player_choice_number==4 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:ʷ����")
		print("����Ӯ��")
	elif comp_number==2 and player_choice_number==4:
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:��")
		print("��Ӯ�ˣ�")
	elif comp_number==3 and player_choice_number==4 :
		print("----------------")
		print("����ѡ��Ϊ:����")
		print("�������ѡ��Ϊ:����")
		print("��Ӯ�ˣ�")
"""
�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

"""


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
name_to_number(choice_name)
rpsls(player_choice_number)
