from sheets_utils import connect_to_sheet, display_sheet_as_table, display_car_info

SHEET = connect_to_sheet()

display_sheet_as_table(SHEET, "stock")

display_car_info(SHEET, "stock", "12")