import os
import tkinter as tk
import tkinter.messagebox as box
from tkinter import ttk
from XML_CScalp import *


class Application:
    def __init__(self):
        box.showwarning(title='Внимание',
                        message='Перед нажатием кнопки "Применить" закройте CScalp.')
        self.root = tk.Tk()
        self.root.resizable(width=0, height=0)  # make window non-resizable
        self.root.title('Глобальная настройка CScalp')
        self.root.eval('tk::PlaceWindow . center')
        self.frame1 = tk.Frame(self.root)
        self.button = tk.Button(self.frame1,
                                text='Применить',
                                font='Verdana 14',
                                bg='light blue',
                                fg='blue',
                                activeforeground='red',
                                activebackground='yellow',
                                relief='groove',
                                command=self.apply_settings)
        tabControl = ttk.Notebook(self.root)
        self.IMG_ON_PATH = os.path.join(os.path.dirname(__file__), 'on.png')
        self.IMG_OFF_PATH = os.path.join(os.path.dirname(__file__), 'off.png')

        self.path_to_settings_files = r'C:\Program Files (x86)\FSR Launcher\SubApps\CScalp\Data\MVS'

        self.tab0_SETTINGS, self.tab1_TRADING, self.tab2_DOM, self.tab3_TICK_PANEL, self.tab4_CLUSTER_PANEL, self.tab5_COMMON_PANEL = self.create_tabs(
            tabControl)

        self.RULER_DATA_TYPE = ('Нет', 'Пункты', 'Проценты')
        self.SHOW_PROFIT_TYPE = ('Пункты', 'Пункты * объем', 'Проценты')
        self.TICKS_STYLE = {'Точки': 'Dots', 'Линии': 'Lines', 'Точки и линии': 'DotsLines'}
        self.TIME_FRAME = {'1m': 1, '5m': 5, '10m': 10, '15m': 15, '30m': 30, '1h': 60, '1d': 1440}
        self.CLUSTER_STYLE_TEXT = {'Сумма покупок и продаж': 'Summ',
                                   'Разница покупок и продаж': 'Delta1',
                                   'Продажи x покупки': 'Delta2'}
        self.CLUSTER_STYLE_COLOR = {'Баланс светлый': 'WhiteBalance',
                                    'Баланс темный': 'BlackBalance',
                                    'Смешение цветов': 'Mix'}

        # spinbox validation
        self.vcmd = (self.root.register(self.validate_spinbox), '%P')
        self.vcmd_len1 = (self.root.register(self.validate_spinbox_len1), '%P')
        self.vcmd_len2 = (self.root.register(self.validate_spinbox_len2), '%P')

        self.fiff_tab_SETTINGS()
        self.fill_tab_TRADING()
        self.fill_tab_DOM()
        self.fill_tab_TICK_PANEL()
        self.fill_tab_CLUSTER_PANEL()
        self.fill_tab_COMMON_PANEL()

        tabControl.pack(expand=1, fill="both")  # ?

        self.button.pack(pady=20)
        self.frame1.pack(side=tk.BOTTOM)

        tk.mainloop()

    def fiff_tab_SETTINGS(self):
        # Поле ввода пути к папке с настроками
        self.set_settings_folder()

    def set_settings_folder(self):
        ttk.Label(self.tab0_SETTINGS,
                  text='Путь к папке с настроками (.tmp-файлами)').grid(row=0, column=0, padx=5, pady=35)

        self.entry_path_to_settings_files = tk.Entry(self.tab0_SETTINGS, width=60)
        self.entry_path_to_settings_files.insert(0, self.path_to_settings_files)
        self.entry_path_to_settings_files.grid(row=1, column=0, padx=25, pady=0)

    def validate_spinbox(self, new_value):
        # Returning True allows the edit to happen, False prevents it.
        return new_value.isdigit()

    def validate_spinbox_len1(self, new_value):
        # Returning True allows the edit to happen, False prevents it.
        return new_value.isdigit() and (len(new_value) == 1)

    def validate_spinbox_len2(self, new_value):
        # Returning True allows the edit to happen, False prevents it.
        return new_value.isdigit() and (len(new_value) == 2)

    def fill_tab_COMMON_PANEL(self):
        # Отображать линию анализа кластеров
        self.show_additive_cursor()

    def show_additive_cursor(self):
        self.lbl = ttk.Label(self.tab5_COMMON_PANEL,
                             text='Отображать линию анализа кластеров').grid(row=0, column=0, padx=5, pady=5)
        self.IMG_OFF1 = tk.PhotoImage(master=self.tab5_COMMON_PANEL,
                                      file=self.IMG_OFF_PATH)
        self.lbl_show_additive_cursor = ttk.Label(self.tab5_COMMON_PANEL, image=self.IMG_OFF1, cursor='hand2')
        self.lbl_show_additive_cursor.grid(row=0, column=1, padx=5, pady=5)
        self.is_show_additive_cursor_on = False
        self.lbl_show_additive_cursor.bind('<Button-1>', self.toggle_show_additive_cursor)

    def toggle_show_additive_cursor(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_show_additive_cursor,
                                        is_label_img_on=self.is_show_additive_cursor_on)

        self.is_show_additive_cursor_on = not self.is_show_additive_cursor_on  # toggle button: on/off

    def fill_tab_CLUSTER_PANEL(self):
        # Показывать панель кластеров
        self.show_cluster_panel(self.tab4_CLUSTER_PANEL)
        # Таймфрейм -- 5 = 5m -- 5 минут
        self.time_frame(self.tab4_CLUSTER_PANEL)
        # Стиль кластеров (текст) -- Summ -- Сумма покупок и продаж
        self.cluster_style_text(self.tab4_CLUSTER_PANEL)
        # Стиль кластеров (цвет) -- BlackBalance -- Баланс темный
        self.cluster_style_color(self.tab4_CLUSTER_PANEL)

    def cluster_style_color(self, tab4_CLUSTER_PANEL):
        ttk.Label(tab4_CLUSTER_PANEL,
                  text='Стиль кластеров (цвет)').grid(row=3, column=0, padx=5, pady=5)
        self.cbx_cluster_style_color = ttk.Combobox(tab4_CLUSTER_PANEL, values=tuple(self.CLUSTER_STYLE_COLOR.keys()),
                                                    state='readonly', width=25)
        self.cbx_cluster_style_color.set('Баланс темный')
        self.cbx_cluster_style_color.grid(row=3, column=1, padx=5, pady=5)

    def cluster_style_text(self, tab4_CLUSTER_PANEL):
        ttk.Label(tab4_CLUSTER_PANEL,
                  text='Стиль кластеров (текст)').grid(row=2, column=0, padx=5, pady=5)
        self.cbx_cluster_style_text = ttk.Combobox(tab4_CLUSTER_PANEL, values=tuple(self.CLUSTER_STYLE_TEXT.keys()),
                                                   state='readonly', width=25)
        self.cbx_cluster_style_text.set('Сумма покупок и продаж')
        self.cbx_cluster_style_text.grid(row=2, column=1, padx=5, pady=5)

    def time_frame(self, tab4_CLUSTER_PANEL):
        ttk.Label(tab4_CLUSTER_PANEL,
                  text='Таймфрейм').grid(row=1, column=0, padx=5, pady=5)
        self.cbx_time_frame = ttk.Combobox(tab4_CLUSTER_PANEL, values=tuple(self.TIME_FRAME.keys()), state='readonly')
        self.cbx_time_frame.set('5m')
        self.cbx_time_frame.grid(row=1, column=1, padx=5, pady=5)

    def show_cluster_panel(self, tab4_CLUSTER_PANEL):
        ttk.Label(tab4_CLUSTER_PANEL,
                  text='Показывать панель кластеров').grid(row=0, column=0, padx=5, pady=5)
        self.IMG_ON = tk.PhotoImage(master=tab4_CLUSTER_PANEL,
                                    file=self.IMG_ON_PATH)
        self.lbl_show_cluster_panel = ttk.Label(tab4_CLUSTER_PANEL, image=self.IMG_ON, cursor='hand2')
        self.lbl_show_cluster_panel.grid(row=0, column=1, padx=5, pady=5)
        self.is_show_cluster_panel_on = True
        self.lbl_show_cluster_panel.bind('<Button-1>', self.toggle_show_cluster_panel)

    def toggle_show_cluster_panel(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_show_cluster_panel,
                                        is_label_img_on=self.is_show_cluster_panel_on)

        self.is_show_cluster_panel_on = not self.is_show_cluster_panel_on  # toggle button: on/off

    def fill_tab_TICK_PANEL(self):
        # Скрывать отфильтрованные тики
        self.hide_filtered_ticks()
        # Уведомление: обнаружен крупный объем
        self.play_big_amount_on_tick()
        # Толщина линии тиков
        self.ticks_weight()
        # Складывать тики за период, мсек
        self.sum_ticks_period()
        # Стиль тиков -- DotsLines -- Точки и линии
        self.ticks_style()

    def sum_ticks_period(self):
        ttk.Label(self.tab3_TICK_PANEL,
                  text='Складывать тики за период, мсек').grid(row=3, column=0, padx=5, pady=5)
        default_value = tk.StringVar()
        default_value.set('300')
        self.sp_SumTicks_Period = tk.Spinbox(self.tab3_TICK_PANEL, from_=0, to=999999, font='Verdana 10',
                                             textvariable=default_value)
        # spinbox validation
        self.sp_SumTicks_Period.configure(validate="key", validatecommand=self.vcmd)
        self.sp_SumTicks_Period.grid(row=3, column=1, padx=5, pady=5)

    def ticks_weight(self):
        ttk.Label(self.tab3_TICK_PANEL,
                  text='Толщина линии тиков').grid(row=2, column=0, padx=5, pady=5)
        self.sp_TicksWeight = tk.Spinbox(self.tab3_TICK_PANEL, from_=1, to=3, font='Verdana 10')
        # spinbox validation
        self.sp_TicksWeight.configure(validate="key", validatecommand=self.vcmd_len1)
        self.sp_TicksWeight.grid(row=2, column=1, padx=5, pady=5)

    def play_big_amount_on_tick(self):
        lbl = ttk.Label(self.tab3_TICK_PANEL,
                        text='Уведомление: обнаружен крупный объем').grid(row=1, column=0, padx=5, pady=5)
        self.IMG_OFF4 = tk.PhotoImage(master=self.tab3_TICK_PANEL,
                                      file=self.IMG_OFF_PATH)
        self.lbl_play_big_amount_on_tick = ttk.Label(self.tab3_TICK_PANEL, image=self.IMG_OFF4, cursor='hand2')
        self.lbl_play_big_amount_on_tick.grid(row=1, column=1, padx=5, pady=5)
        self.is_play_big_amount_on_tick_on = False
        self.lbl_play_big_amount_on_tick.bind('<Button-1>', self.toggle_play_big_amount_on_tick)

    def toggle_play_big_amount_on_tick(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_play_big_amount_on_tick,
                                        is_label_img_on=self.is_play_big_amount_on_tick_on)

        self.is_play_big_amount_on_tick_on = not self.is_play_big_amount_on_tick_on  # toggle button: on/off

    def hide_filtered_ticks(self):
        ttk.Label(self.tab3_TICK_PANEL,
                  text='Скрывать отфильтрованные тики').grid(row=0, column=0, padx=5, pady=5)
        self.IMG_ON1 = tk.PhotoImage(master=self.tab3_TICK_PANEL,
                                     file=self.IMG_ON_PATH)
        self.lbl_hide_filtered_ticks = ttk.Label(self.tab3_TICK_PANEL, image=self.IMG_ON1, cursor='hand2')
        self.lbl_hide_filtered_ticks.grid(row=0, column=1, padx=5, pady=5)
        self.is_hide_filtered_ticks_on = True
        self.lbl_hide_filtered_ticks.bind('<Button-1>', self.toggle_hide_filtered_ticks)

    def toggle_hide_filtered_ticks(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_hide_filtered_ticks,
                                        is_label_img_on=self.is_hide_filtered_ticks_on)

        self.is_hide_filtered_ticks_on = not self.is_hide_filtered_ticks_on  # toggle button: on/off

    def fill_tab_TRADING(self):
        # Дальность заброса
        # лимитных заявок
        self.throw_limit_to(self.tab1_TRADING)
        # Уведомление: совершена сделка
        self.play_sound_on_trade(self.tab1_TRADING)
        # Галочка "Ввод в $"
        self.is_work_amount_in_money_mode(self.tab1_TRADING)
        # Активная клавиша (1 из 5) -- слева внизу стакана
        self.active_work_amount_key(self.tab1_TRADING)
        # Отображение прибыли
        self.show_profit_type(self.tab1_TRADING)

    def show_profit_type(self, tab1_TRADING):
        ttk.Label(tab1_TRADING,
                  text='Отображение прибыли').grid(row=4, column=0, padx=5, pady=5)
        self.cbx_show_profit_type = ttk.Combobox(tab1_TRADING, values=self.SHOW_PROFIT_TYPE, state='readonly')
        self.cbx_show_profit_type.set('Проценты')
        self.cbx_show_profit_type.grid(row=4, column=1, padx=5, pady=5)

    def active_work_amount_key(self, tab1_TRADING):
        ttk.Label(tab1_TRADING,
                  text='Активная клавиша (1 из 5)\n(слева внизу стакана)').grid(row=3, column=0, padx=5, pady=5)
        self.cbx_active_work_amount_key = ttk.Combobox(tab1_TRADING, values=(1, 2, 3, 4, 5), state='readonly')
        self.cbx_active_work_amount_key.set(1)
        self.cbx_active_work_amount_key.grid(row=3, column=1, padx=5, pady=5)

    # Отображать линейку
    def ruler_data_type(self, tab2_DOM):
        ttk.Label(tab2_DOM,
                  text='Отображать линейку').grid(row=5, column=0, padx=5, pady=5)
        self.cbx_ruler_data_type = ttk.Combobox(tab2_DOM, values=self.RULER_DATA_TYPE, state='readonly')
        self.cbx_ruler_data_type.set('Проценты')
        self.cbx_ruler_data_type.grid(row=5, column=1, padx=5, pady=5)

    def fill_tab_DOM(self):
        # Уведомление: обнаружен крупный объем
        self.play_big_amount(self.tab2_DOM)
        # Уведомление: обнаружен крупный объем 2
        self.play_huge_amount(self.tab2_DOM)
        # Автопрокрутка
        self.auto_scroll(self.tab2_DOM)
        # Уведомление: сработал сигнальный уровень
        self.play_user_signal_price_levels(self.tab2_DOM)
        # Высота строки
        self.string_height(self.tab2_DOM)
        # Отображать линейку
        self.ruler_data_type(self.tab2_DOM)

    def ticks_style(self):
        ttk.Label(self.tab3_TICK_PANEL,
                  text='Стиль тиков').grid(row=4, column=0, padx=5, pady=5)
        self.cbx_ticks_style = ttk.Combobox(self.tab3_TICK_PANEL, values=tuple(self.TICKS_STYLE.keys()),
                                            state='readonly')
        self.cbx_ticks_style.set('Точки и линии')
        self.cbx_ticks_style.grid(row=4, column=1, padx=5, pady=5)

    def string_height(self, tab2_DOM):
        ttk.Label(tab2_DOM,
                  text='Высота строки').grid(row=4, column=0, padx=5, pady=5)
        self.sp_StringHeight = tk.Spinbox(tab2_DOM, from_=10, to=25, font='Verdana 10')
        # spinbox validation
        self.sp_StringHeight.configure(validate="key", validatecommand=self.vcmd_len2)
        self.sp_StringHeight.grid(row=4, column=1, padx=5, pady=5)

    def play_user_signal_price_levels(self, tab2_DOM):
        ttk.Label(tab2_DOM,
                  text='Уведомление: сработал сигнальный уровень').grid(row=3, column=0, padx=5, pady=5)
        self.IMG_ON2 = tk.PhotoImage(master=tab2_DOM,
                                     file=self.IMG_ON_PATH)
        self.lbl_play_user_signal_price_levels = ttk.Label(tab2_DOM, image=self.IMG_ON2, cursor='hand2')  #
        self.lbl_play_user_signal_price_levels.grid(row=3, column=1, padx=5, pady=5)
        self.is_play_user_signal_price_levels_on = True
        self.lbl_play_user_signal_price_levels.bind('<Button-1>', self.toggle_play_user_signal_price_levels)

    def toggle_play_user_signal_price_levels(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_play_user_signal_price_levels,
                                        is_label_img_on=self.is_play_user_signal_price_levels_on)

        self.is_play_user_signal_price_levels_on = not self.is_play_user_signal_price_levels_on  # toggle button: on/off

    def auto_scroll(self, tab2_DOM):
        ttk.Label(tab2_DOM,
                  text='Автопрокрутка').grid(row=2, column=0, padx=5, pady=5)
        self.IMG_ON3 = tk.PhotoImage(master=tab2_DOM,
                                     file=self.IMG_ON_PATH)
        self.lbl_auto_scroll = ttk.Label(tab2_DOM, image=self.IMG_ON3, cursor='hand2')
        self.lbl_auto_scroll.grid(row=2, column=1, padx=5, pady=5)
        self.is_auto_scroll_on = True
        self.lbl_auto_scroll.bind('<Button-1>', self.toggle_auto_scroll)

    def toggle_auto_scroll(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_auto_scroll,
                                        is_label_img_on=self.is_auto_scroll_on)

        self.is_auto_scroll_on = not self.is_auto_scroll_on  # toggle button: on/off

    def play_huge_amount(self, tab2_DOM):
        ttk.Label(tab2_DOM,
                  text='Уведомление: обнаружен крупный объем 2').grid(row=1, column=0, padx=5, pady=5)
        self.IMG_OFF2 = tk.PhotoImage(master=tab2_DOM,
                                      file=self.IMG_OFF_PATH)
        self.lbl_play_huge_amount = ttk.Label(tab2_DOM, image=self.IMG_OFF2, cursor='hand2')
        self.lbl_play_huge_amount.grid(row=1, column=1, padx=5, pady=5)
        self.is_play_huge_amount_on = False
        self.lbl_play_huge_amount.bind('<Button-1>', self.toggle_play_huge_amount)

    def toggle_play_huge_amount(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_play_huge_amount,
                                        is_label_img_on=self.is_play_huge_amount_on)

        self.is_play_huge_amount_on = not self.is_play_huge_amount_on  # toggle button: on/off

    def play_big_amount(self, tab2_DOM):
        ttk.Label(tab2_DOM,
                  text='Уведомление: обнаружен крупный объем').grid(row=0, column=0, padx=5, pady=5)
        self.IMG_OFF3 = tk.PhotoImage(master=tab2_DOM,
                                      file=self.IMG_OFF_PATH)
        self.lbl_play_big_amount = ttk.Label(tab2_DOM, image=self.IMG_OFF3, cursor='hand2')
        self.lbl_play_big_amount.grid(row=0, column=1, padx=5, pady=5)
        self.is_play_big_amount_on = False
        self.lbl_play_big_amount.bind('<Button-1>', self.toggle_play_big_amount)

    def toggle_play_big_amount(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_play_big_amount,
                                        is_label_img_on=self.is_play_big_amount_on)

        self.is_play_big_amount_on = not self.is_play_big_amount_on  # toggle button: on/off

    # Галочка "Ввод в $"
    def is_work_amount_in_money_mode(self, tab1_TRADING):
        ttk.Label(tab1_TRADING,
                  text='Галочка "Ввод в $"').grid(row=2, column=0, padx=5, pady=5)
        self.IMG_ON4 = tk.PhotoImage(master=tab1_TRADING,
                                     file=self.IMG_ON_PATH)
        self.lbl_IsWorkAmountInMoneyMode = ttk.Label(tab1_TRADING, image=self.IMG_ON4, cursor='hand2')
        self.lbl_IsWorkAmountInMoneyMode.grid(row=2, column=1, padx=5, pady=5)
        self.isWorkAmountInMoneyMode_on = True
        self.lbl_IsWorkAmountInMoneyMode.bind('<Button-1>', self.toggle_IsWorkAmountInMoneyMode)

    def toggle_IsWorkAmountInMoneyMode(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_IsWorkAmountInMoneyMode,
                                        is_label_img_on=self.isWorkAmountInMoneyMode_on)

        self.isWorkAmountInMoneyMode_on = not self.isWorkAmountInMoneyMode_on  # toggle button: on/off

    def create_tabs(self, tabControl):
        #                                       Вкладки
        tab0_SETTINGS = ttk.Frame(tabControl)  # Настройки
        tab1_TRADING = ttk.Frame(tabControl)  # "Торговля"
        tab2_DOM = ttk.Frame(tabControl)  # "Стакан"
        tab3_TICK_PANEL = ttk.Frame(tabControl)  # "Тики"
        tab4_CLUSTER_PANEL = ttk.Frame(tabControl)  # "Кластеры"
        tab5_COMMON_PANEL = ttk.Frame(tabControl)  # "Общие"
        tabControl.add(tab0_SETTINGS, text='Настройки')
        tabControl.add(tab1_TRADING, text='Торговля')
        tabControl.add(tab2_DOM, text='Стакан')
        tabControl.add(tab3_TICK_PANEL, text='Тики')
        tabControl.add(tab4_CLUSTER_PANEL, text='Кластеры')
        tabControl.add(tab5_COMMON_PANEL, text='Общие')
        return tab0_SETTINGS, tab1_TRADING, tab2_DOM, tab3_TICK_PANEL, tab4_CLUSTER_PANEL, tab5_COMMON_PANEL

    # Уведомление: совершена сделка
    def play_sound_on_trade(self, tab1_TRADING):
        ttk.Label(tab1_TRADING,
                  text='Уведомление: совершена\nсделка').grid(row=1, column=0, padx=5, pady=5)
        self.IMG_ON5 = tk.PhotoImage(master=tab1_TRADING,
                                     file=self.IMG_ON_PATH)
        self.lbl_PlaySoundOnTrade = ttk.Label(tab1_TRADING, image=self.IMG_ON5, cursor='hand2')
        self.lbl_PlaySoundOnTrade.grid(row=1, column=1, padx=5, pady=5)
        self.is_PlaySoundOnTrade_on = True
        self.lbl_PlaySoundOnTrade.bind('<Button-1>', self.toggle_play_sound_on_trade)

    # Дальность заброса лимитных заявок
    def throw_limit_to(self, tab1_TRADING):
        ttk.Label(tab1_TRADING,
                  text='Дальность заброса\nлимитных заявок').grid(row=0, column=0, padx=5, pady=5)
        self.sp_ThrowLimitTo = tk.Spinbox(tab1_TRADING, from_=0, to=100, font='Verdana 10')
        # Spinbox Validation
        self.sp_ThrowLimitTo.configure(validate="key", validatecommand=self.vcmd)
        self.sp_ThrowLimitTo.grid(row=0, column=1, padx=5, pady=5)

    # смена изображения переключателя (вкл/выкл)
    def toggle_switch_on_off_image(self, label, is_label_img_on):
        if is_label_img_on:
            label['image'] = self.IMG_OFF1
        else:
            label['image'] = self.IMG_ON1
        pass

    def toggle_play_sound_on_trade(self, event):
        self.toggle_switch_on_off_image(label=self.lbl_PlaySoundOnTrade,
                                        is_label_img_on=self.is_PlaySoundOnTrade_on)

        self.is_PlaySoundOnTrade_on = not self.is_PlaySoundOnTrade_on  # toggle button: on/off

    def apply_settings(self):

        import glob
        import shutil
        from datetime import datetime, timezone

        utc_dt = datetime.now(timezone.utc)  # UTC time

        self.path_to_tmp_files = self.entry_path_to_settings_files.get()
        os.chdir(self.path_to_tmp_files)
        files = glob.glob('BINAD.CCUR*.tmp')
        path_parent = os.path.dirname(self.path_to_tmp_files)
        str_utc_dt = str(utc_dt).replace(':', '-').replace(' ', '_').replace('+', '_')
        full_file_name = 'xml_settings_backup' + str_utc_dt
        full_path_to_new_dir = os.path.join(path_parent, full_file_name)

        os.mkdir(full_path_to_new_dir)

        for file in files:
            full_path_to_tmp_file = os.path.join(self.path_to_tmp_files, file)
            full_path_to_copy_of_tmp_file = os.path.join(full_path_to_new_dir, file)
            shutil.copyfile(full_path_to_tmp_file, full_path_to_copy_of_tmp_file)

        base_name = os.path.join(self.path_to_tmp_files, full_file_name)
        shutil.make_archive(base_name=base_name, format='zip', root_dir=full_path_to_new_dir)
        shutil.rmtree(path=full_path_to_new_dir)

        files_count = 0

        for file in files:
            if file.startswith('BINAD.CCUR') and file.endswith('.tmp'):

                files_count += 1

                xml = get_xml_content(file)

                try:
                    xml['Settings']['TRADING']['ThrowLimitTo']['@Value'] = self.sp_ThrowLimitTo.get()
                except KeyError:
                    pass
                try:
                    xml['Settings']['TRADING']['PlaySoundOnTrade']['@Value'] = str(self.is_PlaySoundOnTrade_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['TRADING']['IsWorkAmountInMoneyMode']['@Value'] = str(
                        self.is_PlaySoundOnTrade_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['TRADING']['ActiveWorkAmountKey']['@Value'] = str(
                        self.cbx_active_work_amount_key.get())
                except KeyError:
                    pass
                try:
                    str_val = self.cbx_show_profit_type.get()
                    int_val = self.SHOW_PROFIT_TYPE.index(str_val)
                    xml['Settings']['TRADING']['ShowProfitType']['@Value'] = str(int_val)
                except KeyError:
                    pass
                try:
                    xml['Settings']['DOM']['PlayBigAmount']['@Value'] = str(self.is_play_big_amount_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['DOM']['PlayHugeAmount']['@Value'] = str(self.is_play_huge_amount_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['DOM']['AutoScroll']['@Value'] = str(self.is_auto_scroll_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['DOM']['PlayUserSignalPriceLevels']['@Value'] = str(
                        self.is_play_user_signal_price_levels_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['DOM']['StringHeight']['@Value'] = self.sp_StringHeight.get()
                except KeyError:
                    pass
                try:
                    str_val = self.cbx_ruler_data_type.get()
                    int_val = self.RULER_DATA_TYPE.index(str_val)
                    xml['Settings']['DOM']['RulerDataType']['@Value'] = str(int_val)
                except KeyError:
                    pass
                try:
                    xml['Settings']['TICK_PANEL']['HideFilteredTicks']['@Value'] = str(
                        self.is_hide_filtered_ticks_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['TICK_PANEL']['PlayBigAmount']['@Value'] = str(
                        self.is_play_big_amount_on_tick_on)
                except KeyError:
                    pass
                try:
                    xml['Settings']['TICK_PANEL']['TicksWeight']['@Value'] = self.sp_TicksWeight.get()
                except KeyError:
                    pass
                try:
                    xml['Settings']['TICK_PANEL']['SumTicks_Period']['@Value'] = self.sp_SumTicks_Period.get()
                except KeyError:
                    pass
                try:
                    key = self.cbx_ticks_style.get()
                    xml['Settings']['TICK_PANEL']['TicksStyle']['@Value'] = self.TICKS_STYLE[key]
                except KeyError:
                    pass
                try:
                    xml['Settings']['CLUSTER_PANEL']['ShowClusterPanel']['@Value'] = str(
                        self.is_show_cluster_panel_on)
                except KeyError:
                    pass
                try:
                    key = self.cbx_time_frame.get()
                    xml['Settings']['CLUSTER_PANEL']['TimeFrame']['@Value'] = str(self.TIME_FRAME[key])
                except KeyError:
                    pass
                try:
                    key = self.cbx_cluster_style_text.get()
                    xml['Settings']['CLUSTER_PANEL']['ClusterStyleText']['@Value'] = str(self.CLUSTER_STYLE_TEXT[key])
                except KeyError:
                    pass
                try:
                    key = self.cbx_cluster_style_color.get()
                    xml['Settings']['CLUSTER_PANEL']['ClusterStyleColor']['@Value'] = str(self.CLUSTER_STYLE_COLOR[key])
                except KeyError:
                    pass

                try:
                    xml['Settings']['COMMON_PANEL']['ShowAdditiveCursor']['@Value'] = str(
                        self.is_show_additive_cursor_on)
                except KeyError:
                    pass

                content = xml_to_dict_.unparse(xml, pretty=True, short_empty_elements=True, full_document=True,
                                               encoding='utf-8')
                xml_lines = content.split('\n')
                replace_tabs_to_spaces(xml_lines)
                add_space_in_front_of_slash(xml_lines)
                add_newline_char_to_end(xml_lines)
                save_new_content_to_xml(file_name=file,
                                        xml_lines=xml_lines)
        if files_count:
            box.showinfo(title='Информация',
                         message='Все настройки сохранены.\n'
                                 f'Настроено {files_count} файлов (стаканов).\n'
                                 'Можете снова запустить CScalp.')
        else:
            box.showinfo(title='Информация',
                         message=f'Настроено {files_count} файлов (стаканов).\n'
                                 'Можете снова запустить CScalp.')


Application()
