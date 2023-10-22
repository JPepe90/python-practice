import store

def run():
  text_res = store.get_categories()
  store.to_json(text_res)


if __name__ == '__main__':
  run()