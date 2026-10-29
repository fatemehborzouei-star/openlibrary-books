# دریافت اطلاعات کتاب‌ها از OpenLibrary

یک اسکریپت ساده پایتون که اطلاعات کتاب‌ها را از
[API عمومی OpenLibrary](https://openlibrary.org/dev/docs/api/search)
دریافت می‌کند، فقط کتاب‌هایی را که **بعد از سال ۲۰۰۰** منتشر شده‌اند نگه می‌دارد
و ۵۰ کتاب را در یک فایل CSV ذخیره می‌کند.

## ویژگی‌ها

- دریافت داده از API کتابخانه OpenLibrary با استفاده از `requests`
- فیلتر کتاب‌ها بر اساس سال اولین انتشار (بعد از ۲۰۰۰)
- پیمایش خودکار صفحات تا رسیدن به ۵۰ کتاب
- ذخیره خروجی مرتب در CSV (جدیدترین کتاب‌ها در ابتدا)

## پیش‌نیازها

- پایتون نسخه ۳.۸ یا بالاتر
- کتابخانه `requests`

## نصب

```bash
git clone https://github.com/fatemehborzouei-star/openlibrary-books.git
cd openlibrary-books
pip install -r requirements.txt
```

## اجرا

```bash
python fetch_books.py
```

خروجی در فایل `books.csv` ذخیره می‌شود.

## ساختار خروجی

| ستون | توضیح |
|---|---|
| title | عنوان کتاب |
| authors | نویسنده‌ها (جداشده با کاما) |
| first_publish_year | سال اولین انتشار |
| openlibrary_key | شناسه کتاب در OpenLibrary |

## تنظیمات

برای تغییر رفتار برنامه، ثابت‌های ابتدای فایل `fetch_books.py`
(`SEARCH_QUERY`، `TARGET_BOOK_COUNT` و `MIN_YEAR_EXCLUSIVE`) را ویرایش کنید.
