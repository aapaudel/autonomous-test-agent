
# From repo: soimort/you-get
def get_vid_from_url(url):
        """Extracts video ID from URL.
        """
        return match1(url, r'youtu\.be/([^?/]+)') or \
          match1(url, r'youtube\.com/embed/([^/?]+)') or \
          match1(url, r'youtube\.com/v/([^/?]+)') or \
          match1(url, r'youtube\.com/watch/([^/?]+)') or \
          parse_query_param(url, 'v') or \
          parse_query_param(parse_query_param(url, 'u'), 'v')

# From repo: soimort/you-get
def sina_xml_to_url_list(xml_data):
    """str->list
    Convert XML to URL List.
    From Biligrab.
    """
    rawurl = []
    dom = parseString(xml_data)
    for node in dom.getElementsByTagName('durl'):
        url = node.getElementsByTagName('url')[0]
        rawurl.append(url.childNodes[0].data)
    return rawurl

# From repo: soimort/you-get
def makeMimi(upid):
    """From http://cdn37.atwikiimg.com/sitescript/pub/dksitescript/FC2.site.js
    Also com.hps.util.fc2.FC2EncrptUtil.makeMimiLocal
    L110"""
    strSeed = "gGddgPfeaf_gzyr"
    prehash = upid + "_" + strSeed
    return md5(prehash.encode('utf-8')).hexdigest()

# From repo: soimort/you-get
def fc2video_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    """wrapper"""
    #'http://video.fc2.com/en/content/20151021bTVKnbEw'
    #'http://xiaojiadianvideo.asia/content/20151021bTVKnbEw'
    #'http://video.fc2.com/ja/content/20151021bTVKnbEw'
    #'http://video.fc2.com/tw/content/20151021bTVKnbEw'
    hostname = urlparse(url).hostname
    if not ('fc2.com' in hostname or 'xiaojiadianvideo.asia' in hostname):
        return False
    upid = match1(url, r'.+/content/(\w+)')

    fc2video_download_by_upid(upid, output_dir, merge, info_only)

# From repo: soimort/you-get
def dailymotion_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    """Downloads Dailymotion videos by URL.
    """

    html = get_content(rebuilt_url(url))
    info = json.loads(match1(html, r'qualities":({.+?}),"'))
    title = match1(html, r'"video_title"\s*:\s*"([^"]+)"') or \
            match1(html, r'"title"\s*:\s*"([^"]+)"')
    title = unicodize(title)

    for quality in ['1080','720','480','380','240','144','auto']:
        try:
            real_url = info[quality][1]["url"]
            if real_url:
                break
        except KeyError:
            pass

    mime, ext, size = url_info(real_url)

    print_info(site_info, title, mime, size)
    if not info_only:
        download_urls([real_url], title, ext, size, output_dir=output_dir, merge=merge)

# From repo: soimort/you-get
def dictify(r,root=True):
    """http://stackoverflow.com/a/30923963/2946714"""
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

# From repo: soimort/you-get
def ucas_download_single(url, output_dir = '.', merge = False, info_only = False, **kwargs):
    '''video page'''
    html = get_content(url)
    # resourceID is UUID
    resourceID = re.findall( r'resourceID":"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', html)[0]
    assert resourceID != '', 'Cannot find resourceID!'

    title = match1(html, r'<div class="bc-h">(.+)</div>')
    url_lists = _ucas_get_url_lists_by_resourceID(resourceID)
    assert url_lists, 'Cannot find any URL of such class!'
    
    for k, part in enumerate(url_lists):
        part_title = title + '_' + str(k)
        print_info(site_info, part_title, 'flv', 0)
        if not info_only:
            download_urls(part, part_title, 'flv', total_size=None, output_dir=output_dir, merge=merge)

# From repo: soimort/you-get
def ucas_download_playlist(url, output_dir = '.', merge = False, info_only = False, **kwargs):
    '''course page'''
    html = get_content(url)

    parts = re.findall( r'(getplaytitle.do\?.+)"', html)
    assert parts, 'No part found!'

    for part_path in parts:
        ucas_download('http://v.ucas.ac.cn/course/' + part_path, output_dir=output_dir, merge=merge, info_only=info_only)

# From repo: soimort/you-get
def sina_download_by_vid(vid, title=None, output_dir='.', merge=True, info_only=False):
    """Downloads a Sina video by its unique vid.
    http://video.sina.com.cn/
    """
    xml = api_req(vid)
    urls, name, size = video_info(xml)
    if urls is None:
        log.wtf(name)
    title = name
    print_info(site_info, title, 'flv', size)
    if not info_only:
        download_urls(urls, title, 'flv', size, output_dir = output_dir, merge = merge)

# From repo: soimort/you-get
def sina_download_by_vkey(vkey, title=None, output_dir='.', merge=True, info_only=False):
    """Downloads a Sina video by its unique vkey.
    http://video.sina.com/
    """

    url = 'http://video.sina.com/v/flvideo/%s_0.flv' % vkey
    type, ext, size = url_info(url)

    print_info(site_info, title, 'flv', size)
    if not info_only:
        download_urls([url], title, 'flv', size, output_dir = output_dir, merge = merge)

# From repo: soimort/you-get
def sina_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    """Downloads Sina videos by URL.
    """
    if 'news.sina.com.cn/zxt' in url:
        sina_zxt(url, output_dir=output_dir, merge=merge, info_only=info_only, **kwargs)
        return

    vid = match1(url, r'vid=(\d+)')
    if vid is None:
        video_page = get_content(url)
        vid = hd_vid = match1(video_page, r'hd_vid\s*:\s*\'([^\']+)\'')
        if hd_vid == '0':
            vids = match1(video_page, r'[^\w]vid\s*:\s*\'([^\']+)\'').split('|')
            vid = vids[-1]

    if vid is None:
        vid = match1(video_page, r'vid:"?(\d+)"?')
    if vid:
        #title = match1(video_page, r'title\s*:\s*\'([^\']+)\'')
        sina_download_by_vid(vid, output_dir=output_dir, merge=merge, info_only=info_only)
    else:
        vkey = match1(video_page, r'vkey\s*:\s*"([^"]+)"')
        if vkey is None:
            vid = match1(url, r'#(\d+)')
            sina_download_by_vid(vid, output_dir=output_dir, merge=merge, info_only=info_only)
            return
        title = match1(video_page, r'title\s*:\s*"([^"]+)"')
        sina_download_by_vkey(vkey, title=title, output_dir=output_dir, merge=merge, info_only=info_only)

# From repo: soimort/you-get
def yixia_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    """wrapper"""
    hostname = urlparse(url).hostname
    if 'n.miaopai.com' == hostname: 
        smid = match1(url, r'n\.miaopai\.com/media/([^.]+)') 
        miaopai_download_by_smid(smid, output_dir, merge, info_only)
        return
    elif 'miaopai.com' in hostname:  #Miaopai
        yixia_download_by_scid = yixia_miaopai_download_by_scid
        site_info = "Yixia Miaopai"

        scid = match1(url, r'miaopai\.com/show/channel/([^.]+)\.htm') or \
               match1(url, r'miaopai\.com/show/([^.]+)\.htm') or \
               match1(url, r'm\.miaopai\.com/show/channel/([^.]+)\.htm') or \
               match1(url, r'm\.miaopai\.com/show/channel/([^.]+)')

    elif 'xiaokaxiu.com' in hostname:  #Xiaokaxiu
        yixia_download_by_scid = yixia_xiaokaxiu_download_by_scid
        site_info = "Yixia Xiaokaxiu"

        if re.match(r'http://v.xiaokaxiu.com/v/.+\.html', url):  #PC
            scid = match1(url, r'http://v.xiaokaxiu.com/v/(.+)\.html')
        elif re.match(r'http://m.xiaokaxiu.com/m/.+\.html', url):  #Mobile
            scid = match1(url, r'http://m.xiaokaxiu.com/m/(.+)\.html')

    else:
        pass

    yixia_download_by_scid(scid, output_dir, merge, info_only)

# From repo: soimort/you-get
def veoh_download(url, output_dir = '.', merge = False, info_only = False, **kwargs):
    '''Get item_id'''
    if re.match(r'http://www.veoh.com/watch/\w+', url):
        item_id = match1(url, r'http://www.veoh.com/watch/(\w+)')
    elif re.match(r'http://www.veoh.com/m/watch.php\?v=\.*', url):
        item_id = match1(url, r'http://www.veoh.com/m/watch.php\?v=(\w+)')
    else:
        raise NotImplementedError('Cannot find item ID')
    veoh_download_by_id(item_id, output_dir = '.', merge = False, info_only = info_only, **kwargs)

# From repo: soimort/you-get
def veoh_download_by_id(item_id, output_dir = '.', merge = False, info_only = False, **kwargs):
    """Source: Android mobile"""
    webpage_url = 'http://www.veoh.com/m/watch.php?v={item_id}&quality=1'.format(item_id = item_id)

    #grab download URL
    a = get_content(webpage_url, decoded=True)
    url = match1(a, r'<source src="(.*?)\"\W')

    #grab title
    title = match1(a, r'<meta property="og:title" content="([^"]*)"')

    type_, ext, size = url_info(url)
    print_info(site_info, title, type_, size)
    if not info_only:
        download_urls([url], title, ext, total_size=None, output_dir=output_dir, merge=merge)

# From repo: soimort/you-get
def download_by_id(self, vid = '', title = None, output_dir='.', merge=True, info_only=False,**kwargs):
        """self, str->None
        
        Keyword arguments:
        self: self
        vid: The video ID for BokeCC cloud, something like
        FE3BB999594978049C33DC5901307461
        
        Calls the prepare() to download the video.
        
        If no title is provided, this method shall try to find a proper title
        with the information providin within the
        returned content of the API."""

        assert vid

        self.prepare(vid = vid, title = title, **kwargs)

        self.extract(**kwargs)

        self.download(output_dir = output_dir, 
                    merge = merge, 
                    info_only = info_only, **kwargs)

# From repo: soimort/you-get
def get_vid_from_url(self, url):
        """Extracts video ID from live.qq.com.
        """
        hit = re.search(r'live.qq.com/(\d+)', url)
        if hit is not None:
            return hit.group(1)
        hit = re.search(r'live.qq.com/directory/match/(\d+)', url)
        if hit is not None:
            return self.get_room_id_from_url(hit.group(1))
        html = get_content(url)
        room_id = match1(html, r'room_id\":(\d+)')
        if room_id is None:
            log.wtf('Unknown page {}'.format(url))
        return room_id

# From repo: soimort/you-get
def sprint(text, *colors):
    """Format text with color or other effects into ANSI escaped string."""
    return "\33[{}m{content}\33[{}m".format(";".join([str(color) for color in colors]), RESET, content=text) if IS_ANSI_TERMINAL and colors else text

# From repo: soimort/you-get
def print_log(text, *colors):
    """Print a log message to standard error."""
    sys.stderr.write(sprint("{}: {}".format(script_name, text), *colors) + "\n")

# From repo: soimort/you-get
def e(message, exit_code=None):
    """Print an error log message."""
    print_log(message, YELLOW, BOLD)
    if exit_code is not None:
        sys.exit(exit_code)

# From repo: soimort/you-get
def wtf(message, exit_code=1):
    """What a Terrible Failure!"""
    print_log(message, RED, BOLD)
    if exit_code is not None:
        sys.exit(exit_code)
