import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('image', __name__, url_prefix='/image')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('Image.html', imageList= [
            'https://cn.bing.com/th?id=OIP.PO12cKX5DYFyAWh-i7cD7gHaHa&pid=Api&rs=1',
            'https://cn.bing.com/th?id=OIP.xa8XHtx4FFzdKHSanPm-8QHaJ4&pid=Api&rs=1',
            'https://ae01.alicdn.com/kf/HTB1O0eFRXXXXXaBXXXXq6xXFXXXi/mother-daughter-clothes-family-dress-striped-tassel-cotton-dress-for-girls-and-mom-family-matching-clothes.jpg',
            'https://cn.bing.com/th?id=OIP.x8VF-ZbZfEj7jQo5ztvAwQHaHa&pid=Api&rs=1',
            'https://store.muslimamerican.com/v/vspfiles/photos/GPC002-2.jpg',
            'http://moda.com/fashion-history/victorian/victorian-dress-tan-2.jpg',
            'http://weareladies.net/wp-content/uploads/2015/01/fashion_strong_style_color_b82220_women_strong_clothing.jpg',
            'https://www.outfit4events.com/runtime/cache/images/redesignProductFull/mna-1531.JPG',
            'https://cn.bing.com/th?id=OIP.gxrIzcH1E0qyVeihGWwqdAHaKz&pid=Api&rs=1',
            'https://www.metalocus.es/sites/default/files/file-images/metalocus_issey_miyake_ss2016_03.jpg',
            'https://shop.joinclothes.gr/4332-thickbox_default/dress-semizie-square-sleeveless-100-linen.jpg'
        ])

