import webview
import threading


def load_page(window):
    try:
        window.load_url('https://editor.salamlang.ir')
    except Exception as e:
        window.load_html(f'<h1>Error: {str(e)}</h1>')


def on_loaded(window):
    try:
        while True:
            status = window.evaluate_js('document.readyState')
            if status == 'complete':
                print("Page loaded successfully")
                break
    except Exception:
        window.load_html('<h1>Failed to load the page. Please check your connection or try again later.</h1>')


if __name__ == '__main__':
    window = webview.create_window('Salam')
    threading.Thread(target=load_page, args=(window,)).start()
    threading.Thread(target=on_loaded, args=(window,)).start()
    webview.start()
