"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

エラーだけど、こんなふうに呼び出せたらいいなあ

"""

if convert_type = "csv":
    converter = CsvConverter()
elif convert_type = "tsv":
    converter = TsvConverter()
else:
    raise ValueError(f"{convert_type} is invalid.")

# さらに一歩進めてこんなのはどう？
converter = CreateConverter(format)

output = converter.convert(data)
