#%%
import requests

# "https://music.163.com/weapi/cloudsearch/get/web?csrf_token=", body=list()
resp = requests.post(
    "https://music.163.com/weapi/cloudsearch/get/web?csrf_token=",
    data={
        "params": "e+f7PY7zVaw3ANYt8nggFYipZCnr6/dU+Wo9/2S9VyvR4a1fqwijrBaFfGyEOljPJa1jYsZKER5VnNXYnZ0OhgILwTFgK0hG31rf/DeltLSY9GoZTS6CXQL2w8VYom17YydwyoeQuAWgAdUVQqWMaBClVvpFqCuGVVWUkWSxFKRygwt32u6M+gkiaJjdduFDQBVCyzaNp0m4aAC1jq/+jAR04SP+rKNxXQAsFc5FyIKp5sCUvd5lrelWOXToClKZx3/xd9nHyYUKbc95OVNk02OfQLxp6eCmng8hHpAHe+pqmutlFzRXk45bfRqO2Fn1jOBxQdvbtp44Xmhda6h4WVxmjURfnPig/IrIB25mk9A=",
        "encSecKey": "43f8e5540b855f2022014d5ea66c632f93141186061531016cb91c46a1663256ea7665455961e2417b3c73124b6bcb3dd9da54539eda0575cb51e971ec37c3a4d99719818e94e3fa7c19a7fc1ebc2e7acb6171839a1781696d5cbee460fe6131e6b94c2a62e45e8714b4ac92ec94ba4963da7efc7f0ca04323813e280865f9e1",
    },
)
resp
# %%
resp.text
# %%
resp.request.body

# %%
