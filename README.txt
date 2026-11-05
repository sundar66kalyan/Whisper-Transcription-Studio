FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2026-11-02-git-b034eb5e7e-full_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/b034eb5e7e

External Assets
frei0r plugins:   https://www.gyan.dev/ffmpeg/builds/ffmpeg-frei0r-plugins
lensfun database: https://www.gyan.dev/ffmpeg/builds/ffmpeg-lensfun-db
whisper models:   https://huggingface.co/ggerganov/whisper.cpp/tree/main

git-full build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
CLMUL enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
6 registers available     yes
7 registers available     yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
experimental features     yes
xmllint enabled           yes

External libraries:
avisynth                libharfbuzz             libsvtjpegxs
bzlib                   libilbc                 libtheora
cairo                   libjxl                  libtwolame
chromaprint             liblc3                  libuavs3d
frei0r                  liblcevc_dec            libvidstab
gmp                     liblensfun              libvmaf
gnutls                  libmodplug              libvo_amrwbenc
iconv                   libmp3lame              libvorbis
ladspa                  libmysofa               libvpx
lcms2                   liboapv                 libvvenc
libaom                  libopencolorio          libwebp
libaribb24              libopencore_amrnb       libx264
libaribcaption          libopencore_amrwb       libx265
libass                  libopenjpeg             libxavs2
libastcenc              libopenmpt              libxevd
libbluray               libopus                 libxeve
libbs2b                 libplacebo              libxml2
libcaca                 libqrencode             libxvid
libcdio                 libquirc                libzimg
libcodec2               librabbitmq             libzmq
libdav1d                librav1e                libzvbi
libdavs2                librist                 lzma
libdvdnav               librubberband           mediafoundation
libdvdread              libshine                openal
libflite                libsnappy               sdl2
libfontconfig           libsoxr                 vapoursynth
libfreetype             libspeex                whisper
libfribidi              libsrt                  zlib
libgme                  libssh
libgsm                  libsvtav1

External libraries providing hardware acceleration:
amf                     d3d12va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               opencl
cuvid                   libmfx                  vaapi
d3d11va                 libvpl                  vulkan

Libraries:
avcodec                 avformat                swscale
avdevice                avutil
avfilter                swresample

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     flv                     pcm_u16le
aac_fixed               fmvc                    pcm_u24be
aac_latm                fourxm                  pcm_u24le
aasc                    fraps                   pcm_u32be
ac3                     frwu                    pcm_u32le
ac3_fixed               ftr                     pcm_u8
acelp_kelvin            g2m                     pcm_vidc
adpcm_4xm               g723_1                  pcx
adpcm_adx               g728                    pdv
adpcm_afc               g729                    pfm
adpcm_agm               gdv                     pgm
adpcm_aica              gem                     pgmyuv
adpcm_argo              gif                     pgssub
adpcm_circus            gremlin_dpcm            pgx
adpcm_ct                gsm                     phm
adpcm_dtk               gsm_ms                  photocd
adpcm_ea                h261                    pictor
adpcm_ea_maxis_xa       h263                    pixlet
adpcm_ea_r1             h263i                   pjs
adpcm_ea_r2             h263p                   png
adpcm_ea_r3             h264                    ppm
adpcm_ea_xas            h264_amf                prores
adpcm_g722              h264_cuvid              prores_raw
adpcm_g726              h264_qsv                prosumer
adpcm_g726le            hap                     psd
adpcm_ima_acorn         hca                     ptx
adpcm_ima_alp           hcom                    qcelp
adpcm_ima_amv           hdr                     qdm2
adpcm_ima_apc           hevc                    qdmc
adpcm_ima_apm           hevc_amf                qdraw
adpcm_ima_citrix        hevc_cuvid              qoa
adpcm_ima_cunning       hevc_qsv                qoi
adpcm_ima_dat4          hnm4_video              qpeg
adpcm_ima_dk3           hq_hqa                  qtrle
adpcm_ima_dk4           hqx                     r10k
adpcm_ima_ea_eacs       huffyuv                 r210
adpcm_ima_ea_sead       hymt                    ra_144
adpcm_ima_escape        iac                     ra_288
adpcm_ima_hvqm2         idcin                   ralf
adpcm_ima_hvqm4         idf                     rasc
adpcm_ima_iss           iff_ilbm                rawvideo
adpcm_ima_magix         ilbc                    realtext
adpcm_ima_moflex        imc                     rka
adpcm_ima_mtf           imm4                    rl2
adpcm_ima_oki           imm5                    roq
adpcm_ima_pda           imm6                    roq_dpcm
adpcm_ima_qt            indeo2                  rpza
adpcm_ima_rad           indeo3                  rscc
adpcm_ima_smjpeg        indeo4                  rtv1
adpcm_ima_ssi           indeo5                  rv10
adpcm_ima_wav           interplay_acm           rv20
adpcm_ima_ws            interplay_dpcm          rv30
adpcm_ima_xbox          interplay_video         rv40
adpcm_ms                ipu                     rv60
adpcm_mtaf              jacosub                 rw2
adpcm_n64               jpeg2000                s302m
adpcm_psx               jpegls                  sami
adpcm_psxc              jv                      sanm
adpcm_rhetorex          kgv1                    sbc
adpcm_sanyo             kmvc                    scpr
adpcm_sbpro_2           lagarith                screenpresso
adpcm_sbpro_3           lead                    sdx2_dpcm
adpcm_sbpro_4           libaom_av1              sga
adpcm_swf               libaribb24              sgi
adpcm_thp               libaribcaption          sgirle
adpcm_thp_le            libastcenc              sheervideo
adpcm_vima              libcodec2               shorten
adpcm_xa                libdav1d                simbiosis_imx
adpcm_xmd               libdavs2                sipr
adpcm_yamaha            libgsm                  siren
adpcm_zork              libgsm_ms               smackaud
agm                     libilbc                 smacker
ahx                     libjxl                  smc
aic                     libjxl_anim             smvjpeg
alac                    liblc3                  snow
alias_pix               libopencore_amrnb       sol_dpcm
als                     libopencore_amrwb       sp5x
amrnb                   libopus                 speedhq
amrwb                   libspeex                speex
amv                     libsvtjpegxs            srgc
anm                     libuavs3d               srt
ansi                    libvorbis               ssa
anull                   libvpx_vp8              stl
apac                    libvpx_vp9              subrip
ape                     libxevd                 subviewer
apng                    libzvbi_teletext        subviewer1
aptx                    loco                    sunrast
aptx_hd                 lscr                    svq1
apv                     m101                    svq3
arbc                    mace3                   tak
argo                    mace6                   targa
ass                     magicyuv                targa_y216
asv1                    mdec                    tdsc
asv2                    media100                text
atrac1                  metasound               theora
atrac3                  microdvd                thp
atrac3al                mimic                   tiertexseqvideo
atrac3p                 misc4                   tiff
atrac3pal               mjpeg                   tmv
atrac9                  mjpeg_cuvid             truehd
aura                    mjpeg_qsv               truemotion1
aura2                   mjpegb                  truemotion2
av1                     mlp                     truemotion2rt
av1_amf                 mmvideo                 truespeech
av1_cuvid               mobiclip                tscc
av1_qsv                 motionpixels            tscc2
avrn                    movtext                 tta
avrp                    mp1                     twinvq
avs                     mp1float                txd
avui                    mp2                     ulti
bethsoftvid             mp2float                utvideo
bfi                     mp3                     v210
bink                    mp3adu                  v210x
binkaudio_dct           mp3adufloat             vb
binkaudio_rdft          mp3float                vble
bintext                 mp3on4                  vbn
bitpacked               mp3on4float             vc1
bmp                     mpc7                    vc1_cuvid
bmv_audio               mpc8                    vc1_qsv
bmv_video               mpeg1_cuvid             vc1image
bonk                    mpeg1video              vcr1
brender_pix             mpeg2_cuvid             vmdaudio
c93                     mpeg2_qsv               vmdvideo
cavs                    mpeg2video              vmix
cbd2_dpcm               mpeg4                   vmnc
ccaption                mpeg4_cuvid             vnull
cdgraphics              mpegvideo               vorbis
cdtoons                 mpl2                    vp3
cdxl                    msa1                    vp4
cfhd                    mscc                    vp5
cinepak                 msmpeg4v1               vp6
clearvideo              msmpeg4v2               vp6a
cljr                    msmpeg4v3               vp6f
cllc                    msnsiren                vp7
comfortnoise            msp2                    vp8
cook                    msrle                   vp8_cuvid
cpia                    mss1                    vp8_qsv
cri                     mss2                    vp9
cscd                    msvideo1                vp9_amf
cyuv                    mszh                    vp9_cuvid
dca                     mts2                    vp9_qsv
dds                     mv30                    vplayer
derf_dpcm               mvc1                    vqa
dfa                     mvc2                    vqc
dfpwm                   mvdv                    vvc
dirac                   mvha                    vvc_qsv
dnxhd                   mwsc                    wady_dpcm
dolby_e                 mxpeg                   wavarc
dpx                     nellymoser              wavpack
dsd_lsbf                notchlc                 wbmp
dsd_lsbf_planar         nuv                     wcmv
dsd_msbf                on2avc                  webp
dsd_msbf_planar         opus                    webp_anim
dsicinaudio             osq                     webvtt
dsicinvideo             paf_audio               wmalossless
dss_sp                  paf_video               wmapro
dst                     pam                     wmav1
dvaudio                 pbm                     wmav2
dvbsub                  pcm_alaw                wmavoice
dvdsub                  pcm_bluray              wmv1
dvvideo                 pcm_dvd                 wmv2
dxa                     pcm_dvda                wmv3
dxtory                  pcm_f16le               wmv3image
dxv                     pcm_f24le               wnv1
eac3                    pcm_f32be               wrapped_avframe
eacmv                   pcm_f32le               ws_snd1
eamad                   pcm_f64be               xan_dpcm
eatgq                   pcm_f64le               xan_wc3
eatgv                   pcm_lxf                 xan_wc4
eatqi                   pcm_mulaw               xbin
eightbps                pcm_s16be               xbm
eightsvx_exp            pcm_s16be_planar        xface
eightsvx_fib            pcm_s16le               xl
escape124               pcm_s16le_planar        xma1
escape130               pcm_s24be               xma2
evrc                    pcm_s24daud             xpm
exr                     pcm_s24le               xsub
fastaudio               pcm_s24le_planar        xwd
ffv1                    pcm_s32be               y41p
ffvhuff                 pcm_s32le               ylc
ffwavesynth             pcm_s32le_planar        yop
fic                     pcm_s64be               yuv4
fits                    pcm_s64le               zero12v
flac                    pcm_s8                  zerocodec
flashsv                 pcm_s8_planar           zlib
flashsv2                pcm_sga                 zmbv
flic                    pcm_u16be

Enabled encoders:
a64multi                hevc_d3d12va            pcm_s32be
a64multi5               hevc_mf                 pcm_s32le
aac                     hevc_nvenc              pcm_s32le_planar
aac_mf                  hevc_qsv                pcm_s64be
ac3                     hevc_vaapi              pcm_s64le
ac3_fixed               hevc_vulkan             pcm_s8
ac3_mf                  huffyuv                 pcm_s8_planar
adpcm_adx               jpeg2000                pcm_u16be
adpcm_argo              jpegls                  pcm_u16le
adpcm_g722              libaom_av1              pcm_u24be
adpcm_g726              libastcenc              pcm_u24le
adpcm_g726le            libcodec2               pcm_u32be
adpcm_ima_alp           libgsm                  pcm_u32le
adpcm_ima_amv           libgsm_ms               pcm_u8
adpcm_ima_apm           libilbc                 pcm_vidc
adpcm_ima_qt            libjxl                  pcx
adpcm_ima_ssi           libjxl_anim             pdv
adpcm_ima_wav           liblc3                  pfm
adpcm_ima_ws            libmp3lame              pgm
adpcm_ms                liboapv                 pgmyuv
adpcm_swf               libopencore_amrnb       phm
adpcm_yamaha            libopenjpeg             png
alac                    libopus                 ppm
alias_pix               librav1e                prores
amv                     libshine                prores_aw
anull                   libspeex                prores_ks
apng                    libsvtav1               prores_ks_vulkan
aptx                    libsvtjpegxs            qoi
aptx_hd                 libtheora               qtrle
apv_vulkan              libtwolame              r10k
ass                     libvo_amrwbenc          r210
asv1                    libvorbis               ra_144
asv2                    libvpx_vp8              rawvideo
av1_amf                 libvpx_vp9              roq
av1_d3d12va             libvvenc                roq_dpcm
av1_mf                  libwebp                 rpza
av1_nvenc               libwebp_anim            rv10
av1_qsv                 libx264                 rv20
av1_vaapi               libx264rgb              s302m
av1_vulkan              libx265                 sbc
avrp                    libxavs2                sgi
avui                    libxeve                 smc
bitpacked               libxvid                 snow
bmp                     ljpeg                   speedhq
cfhd                    magicyuv                srt
cinepak                 mjpeg                   ssa
cljr                    mjpeg_qsv               subrip
comfortnoise            mjpeg_vaapi             sunrast
dca                     mlp                     svq1
dfpwm                   movtext                 targa
dnxhd                   mp2                     text
dpx                     mp2fixed                tiff
dsd_msbf                mp3_mf                  truehd
dvbsub                  mpeg1video              tta
dvdsub                  mpeg2_qsv               ttml
dvvideo                 mpeg2_vaapi             utvideo
dxv                     mpeg2video              v210
eac3                    mpeg4                   vbn
exr                     msmpeg4v2               vc2
ffv1                    msmpeg4v3               vnull
ffv1_vulkan             msrle                   vorbis
ffvhuff                 msvideo1                vp8_vaapi
fits                    nellymoser              vp9_qsv
flac                    opus                    vp9_vaapi
flashsv                 pam                     wavpack
flashsv2                pbm                     wbmp
flv                     pcm_alaw                webvtt
g723_1                  pcm_bluray              wmav1
gif                     pcm_dvd                 wmav2
h261                    pcm_f32be               wmv1
h263                    pcm_f32le               wmv2
h263p                   pcm_f64be               wrapped_avframe
h264_amf                pcm_f64le               xbm
h264_d3d12va            pcm_mulaw               xface
h264_mf                 pcm_s16be               xsub
h264_nvenc              pcm_s16be_planar        xwd
h264_qsv                pcm_s16le               y41p
h264_vaapi              pcm_s16le_planar        yuv4
h264_vulkan             pcm_s24be               zlib
hap                     pcm_s24daud             zmbv
hdr                     pcm_s24le
hevc_amf                pcm_s24le_planar

Enabled hwaccels:
apv_vulkan              hevc_nvdec              vc1_nvdec
av1_d3d11va             hevc_nvdec_cuarray      vc1_nvdec_cuarray
av1_d3d11va2            hevc_vaapi              vc1_vaapi
av1_d3d12va             hevc_vulkan             vp8_nvdec
av1_dxva2               mjpeg_nvdec             vp8_nvdec_cuarray
av1_nvdec               mjpeg_vaapi             vp8_vaapi
av1_nvdec_cuarray       mpeg1_nvdec             vp9_d3d11va
av1_vaapi               mpeg1_nvdec_cuarray     vp9_d3d11va2
av1_vulkan              mpeg2_d3d11va           vp9_d3d12va
dpx_vulkan              mpeg2_d3d11va2          vp9_dxva2
ffv1_vulkan             mpeg2_d3d12va           vp9_nvdec
h263_vaapi              mpeg2_dxva2             vp9_nvdec_cuarray
h264_d3d11va            mpeg2_nvdec             vp9_vaapi
h264_d3d11va2           mpeg2_nvdec_cuarray     vp9_vulkan
h264_d3d12va            mpeg2_vaapi             vvc_vaapi
h264_dxva2              mpeg4_nvdec             wmv3_d3d11va
h264_nvdec              mpeg4_nvdec_cuarray     wmv3_d3d11va2
h264_nvdec_cuarray      mpeg4_vaapi             wmv3_d3d12va
h264_vaapi              prores_raw_vulkan       wmv3_dxva2
h264_vulkan             prores_vulkan           wmv3_nvdec
hevc_d3d11va            vc1_d3d11va             wmv3_nvdec_cuarray
hevc_d3d11va2           vc1_d3d11va2            wmv3_vaapi
hevc_d3d12va            vc1_d3d12va
hevc_dxva2              vc1_dxva2

Enabled parsers:
aac                     dvdsub                  mpegaudio
aac_latm                evc                     mpegvideo
ac3                     ffv1                    opus
adx                     flac                    png
ahx                     ftr                     pnm
amr                     g723_1                  prores
apv                     g729                    prores_raw
av1                     gif                     qoi
avs2                    gsm                     rv34
avs3                    h261                    rw2
bmp                     h263                    sbc
cavsvideo               h264                    sipr
cook                    hdr                     tak
cri                     hevc                    vc1
dca                     ipu                     vorbis
dirac                   jpeg2000                vp3
dnxhd                   jpegxl                  vp8
dnxuc                   jpegxs                  vp9
dolby_e                 lcevc                   vvc
dpx                     misc4                   webp
dvaudio                 mjpeg                   xbm
dvbsub                  mlp                     xma
dvd_nav                 mpeg4video              xwd

Enabled demuxers:
aa                      idf                     pcm_f32le
aac                     iff                     pcm_f64be
aax                     ifv                     pcm_f64le
ac3                     ilbc                    pcm_mulaw
ac4                     image2                  pcm_s16be
ace                     image2_alias_pix        pcm_s16le
acm                     image2_brender_pix      pcm_s24be
act                     image2pipe              pcm_s24le
adf                     image_bmp_pipe          pcm_s32be
adp                     image_cri_pipe          pcm_s32le
ads                     image_dds_pipe          pcm_s8
adx                     image_dpx_pipe          pcm_u16be
aea                     image_exr_pipe          pcm_u16le
afc                     image_gem_pipe          pcm_u24be
aiff                    image_gif_pipe          pcm_u24le
aix                     image_hdr_pipe          pcm_u32be
alp                     image_j2k_pipe          pcm_u32le
amr                     image_jpeg_pipe         pcm_u8
amrnb                   image_jpegls_pipe       pcm_vidc
amrwb                   image_jpegxl_pipe       pdv
anm                     image_jpegxs_pipe       pjs
apac                    image_pam_pipe          pmp
apc                     image_pbm_pipe          pp_bnk
ape                     image_pcx_pipe          pva
apm                     image_pfm_pipe          pvf
apng                    image_pgm_pipe          qcp
aptx                    image_pgmyuv_pipe       qoa
aptx_hd                 image_pgx_pipe          r3d
apv                     image_phm_pipe          rawvideo
aqtitle                 image_photocd_pipe      rcwt
argo_asf                image_pictor_pipe       realtext
argo_brp                image_png_pipe          redspark
argo_cvg                image_ppm_pipe          rka
asf                     image_psd_pipe          rl2
ass                     image_qdraw_pipe        rm
ast                     image_qoi_pipe          roq
astc                    image_rw2_pipe          rpl
au                      image_sgi_pipe          rsd
av1                     image_sunrast_pipe      rso
avi                     image_svg_pipe          rtp
avisynth                image_tiff_pipe         rtsp
avr                     image_vbn_pipe          s337m
avs                     image_webp_pipe         sami
avs2                    image_xbm_pipe          sap
avs3                    image_xpm_pipe          sbc
bethsoftvid             image_xwd_pipe          sbg
bfi                     imf                     scc
bfstm                   ingenient               scd
bink                    ipmovie                 sdns
binka                   ipu                     sdp
bintext                 ircam                   sdr2
bit                     iss                     sds
bitpacked               iv8                     sdx
bmv                     ivf                     segafilm
boa                     ivr                     ser
bonk                    jacosub                 sga
brstm                   jpeg_mpf                shorten
c93                     jpegxl_anim             siff
caf                     jv                      simbiosis_imx
cavsvideo               ktx                     sln
cdg                     kux                     smacker
cdxl                    kvag                    smjpeg
cine                    laf                     smush
codec2                  lc3                     sol
codec2raw               lcevc                   sox
concat                  libgme                  spdif
dash                    libmodplug              srt
data                    libopenmpt              stl
daud                    live_flv                str
dcstr                   lmlm4                   subviewer
derf                    loas                    subviewer1
dfa                     lrc                     sup
dfpwm                   luodat                  svag
dhav                    lvf                     svs
dirac                   lxf                     swf
dnxhd                   m4v                     tak
dsf                     matroska                tedcaptions
dsicin                  mca                     thp
dss                     mcc                     threedostr
dts                     mgsts                   tiertexseq
dtshd                   microdvd                tmv
dv                      mjpeg                   truehd
dvbsub                  mjpeg_2000              tta
dvbtxt                  mlp                     tty
dvdvideo                mlv                     txd
dxa                     mm                      ty
ea                      mmf                     usm
ea_cdata                mods                    v210
eac3                    moflex                  v210x
epaf                    mov                     vag
evc                     mp3                     vapoursynth
ffmetadata              mpc                     vc1
filmstrip               mpc8                    vc1t
fits                    mpegps                  vividas
flac                    mpegts                  vivo
flic                    mpegtsraw               vmd
flv                     mpegvideo               vobsub
fourxm                  mpjpeg                  voc
frm                     mpl2                    vpk
fsb                     mpsub                   vplayer
fwse                    msf                     vqf
g722                    msnwc_tcp               vvc
g723_1                  msp                     w64
g726                    mtaf                    wady
g726le                  mtv                     wav
g728                    musx                    wavarc
g729                    mv                      wc3
gdv                     mvi                     webm_dash_manifest
genh                    mvr                     webp_anim
gif                     mxf                     webvtt
gsm                     mxg                     wsaud
gxf                     nc                      wsd
h261                    nistsphere              wsvqa
h263                    nsp                     wtv
h264                    nsv                     wv
hca                     nut                     wve
hcom                    nuv                     xa
hevc                    obu                     xbin
hls                     ogg                     xmd
hnm                     oma                     xmv
hxvs                    osq                     xvag
iamf                    paf                     xwma
ico                     pcm_alaw                yop
idcin                   pcm_f32be               yuv4mpegpipe

Enabled muxers:
a64                     h264                    pcm_s16le
ac3                     hash                    pcm_s24be
ac4                     hds                     pcm_s24le
adts                    hevc                    pcm_s32be
adx                     hls                     pcm_s32le
aea                     iamf                    pcm_s8
aiff                    ico                     pcm_u16be
alp                     ilbc                    pcm_u16le
amr                     image2                  pcm_u24be
amv                     image2pipe              pcm_u24le
apm                     ipod                    pcm_u32be
apng                    ircam                   pcm_u32le
aptx                    ismv                    pcm_u8
aptx_hd                 iterm2                  pcm_vidc
apv                     ivf                     pdv
argo_asf                jacosub                 psp
argo_cvg                jpeg_mpf                rawvideo
asf                     ktx                     rcwt
asf_stream              kvag                    rm
ass                     latm                    roq
ast                     lc3                     rso
astc                    lcevc                   rtp
au                      lrc                     rtp_mpegts
avi                     m4v                     rtsp
avif                    matroska                sap
avm2                    matroska_audio          sbc
avs2                    mcc                     scc
avs3                    md5                     segafilm
bit                     microdvd                segment
caf                     mjpeg                   smjpeg
cavsvideo               mkvtimestamp_v2         smoothstreaming
chromaprint             mlp                     sox
codec2                  mmf                     spdif
codec2raw               mov                     spx
crc                     mp2                     srt
dash                    mp3                     stream_segment
data                    mp4                     streamhash
daud                    mpeg1system             sup
dfpwm                   mpeg1vcd                swf
dirac                   mpeg1video              tee
dnxhd                   mpeg2dvd                tg2
dts                     mpeg2svcd               tgp
dv                      mpeg2video              truehd
eac3                    mpeg2vob                tta
evc                     mpegts                  ttml
f4v                     mpjpeg                  uncodedframecrc
ffmetadata              mxf                     vc1
fifo                    mxf_d10                 vc1t
filmstrip               mxf_opatom              voc
fits                    null                    vvc
flac                    nut                     w64
flv                     obu                     wav
framecrc                oga                     webm
framehash               ogg                     webm_chunk
framemd5                ogv                     webm_dash_manifest
g722                    oma                     webp
g723_1                  opus                    webvtt
g726                    pcm_alaw                whip
g726le                  pcm_f32be               wsaud
gif                     pcm_f32le               wtv
gsm                     pcm_f64be               wv
gxf                     pcm_f64le               yuv4mpegpipe
h261                    pcm_mulaw
h263                    pcm_s16be

Enabled protocols:
async                   httpproxy               rtmpe
bluray                  https                   rtmps
cache                   icecast                 rtmpt
concat                  ipfs_gateway            rtmpte
concatf                 ipns_gateway            rtmpts
crypto                  libamqp                 rtp
data                    librist                 shared
dtls                    libsrt                  srtp
fd                      libssh                  subfile
ffrtmpcrypt             libzmq                  tcp
ffrtmphttp              md5                     tee
file                    mmsh                    tls
ftp                     mmst                    udp
gopher                  pipe                    udplite
gophers                 prompeg                 windows_handle
http                    rtmp

Enabled filters:
a3dscope                deesser                 pan
aap                     deflate                 perlin
abench                  deflicker               perms
abitscope               deinterlace_d3d12       perspective
acompressor             deinterlace_qsv         phase
acontrast               deinterlace_vaapi       photosensitivity
acopy                   dejudder                pixdesctest
acrossfade              delogo                  pixelize
acrossover              denoise_vaapi           pixscope
acrusher                deshake                 pp7
acue                    deshake_opencl          premultiply
addroi                  despill                 premultiply_dynamic
adeclick                detelecine              prewitt
adeclip                 dialoguenhance          prewitt_opencl
adecorrelate            dilation                procamp_vaapi
adelay                  dilation_opencl         program_opencl
adenorm                 displace                pseudocolor
aderivative             doubleweave             psnr
adrawgraph              drawbox                 pullup
adrc                    drawbox_vaapi           qp
adynamicequalizer       drawgraph               qrencode
adynamicsmooth          drawgrid                qrencodesrc
aecho                   drawtext                quirc
aemphasis               drawvg                  random
aeval                   drmeter                 readeia608
aevalsrc                dynaudnorm              readvitc
aexciter                earwax                  realtime
afade                   ebur128                 remap
afdelaysrc              edgedetect              remap_opencl
afftdn                  elbg                    removegrain
afftfilt                entropy                 removelogo
afir                    epx                     repeatfields
afireqsrc               eq                      replaygain
afirsrc                 equalizer               reverse
aformat                 erosion                 rgbashift
afreqshift              erosion_opencl          rgbtestsrc
afwtdn                  estdif                  roberts
agate                   exposure                roberts_opencl
agraphmonitor           extractplanes           rotate
ahistogram              extrastereo             rubberband
aiir                    fade                    sab
aintegral               feedback                scale
ainterleave             fftdnoiz                scale2ref
alatency                fftfilt                 scale_cuda
alimiter                field                   scale_d3d11
allpass                 fieldhint               scale_d3d12
allrgb                  fieldmatch              scale_qsv
allyuv                  fieldorder              scale_vaapi
aloop                   fillborders             scale_vulkan
alphaextract            find_rect               scdet
alphamerge              firequalizer            scdet_vulkan
amerge                  flanger                 scharr
ametadata               flip_vulkan             scroll
amf_capture             flite                   segment
amix                    floodfill               select
amovie                  format                  selectivecolor
amplify                 fps                     sendcmd
amultiply               framepack               separatefields
anequalizer             framerate               setdar
anlmdn                  framestep               setfield
anlmf                   frc_amf                 setparams
anlms                   freezedetect            setpts
anoisesrc               freezeframes            setrange
anull                   frei0r                  setsar
anullsink               frei0r_src              settb
anullsrc                fruc_vulkan             sharpness_vaapi
apad                    fspp                    shear
aperms                  fsync                   showcqt
aphasemeter             gainmap                 showcwt
aphaser                 gblur                   showfreqs
aphaseshift             gblur_vulkan            showinfo
apsnr                   geq                     showpalette
apsyclip                gfxcapture              showspatial
apulsator               gradfun                 showspectrum
arealtime               gradients               showspectrumpic
aresample               graphmonitor            showvolume
areverse                grayworld               showwaves
arls                    greyedge                showwavespic
arnndn                  guided                  shuffleframes
asdr                    haas                    shufflepixels
asegment                haldclut                shuffleplanes
aselect                 haldclutsrc             sidechaincompress
asendcmd                hdcd                    sidechaingate
asetnsamples            headphone               sidedata
asetpts                 hflip                   sierpinski
asetrate                hflip_vulkan            signalstats
asettb                  highpass                signature
ashowinfo               highshelf               silencedetect
asidedata               hilbert                 silenceremove
asisdr                  histeq                  sinc
asoftclip               histogram               sine
aspectralstats          hqdn3d                  siti
asplit                  hqx                     smartblur
ass                     hstack                  smptebars
astats                  hstack_qsv              smptehdbars
astreamselect           hstack_vaapi            sobel
asubboost               hsvhold                 sobel_opencl
asubcut                 hsvkey                  sofalizer
asupercut               hue                     spectrumsynth
asuperpass              huesaturation           speechnorm
asuperstop              hwdownload              split
atadenoise              hwmap                   spp
atempo                  hwupload                sr_amf
atilt                   hwupload_cuda           ssim
atrim                   hysteresis              ssim360
avectorscope            iccdetect               stereo3d
avgblur                 iccgen                  stereotools
avgblur_opencl          identity                stereowiden
avgblur_vulkan          idet                    streamselect
avsynctest              il                      subtitles
axcorrelate             inflate                 super2xsai
azmq                    interlace               superequalizer
backgroundkey           interlace_vulkan        surround
bandpass                interleave              swaprect
bandreject              join                    swapuv
bass                    kerndeint               tblend
bbox                    kirsch                  telecine
bench                   ladspa                  testsrc
bilateral               lagfun                  testsrc2
bilateral_cuda          latency                 thistogram
biquad                  latticepal              threshold
bitplanenoise           lcevc                   thumbnail
blackdetect             lenscorrection          thumbnail_cuda
blackdetect_vulkan      lensfun                 tile
blackframe              libplacebo              tiltandshift
blend                   libplacebo_scene        tiltshelf
blend_vulkan            libvmaf                 tinterlace
blockdetect             life                    tlut2
blurdetect              limitdiff               tmedian
bm3d                    limiter                 tmidequalizer
boxblur                 loop                    tmix
boxblur_opencl          loudnorm                tonemap
bs2b                    lowpass                 tonemap_opencl
bwdif                   lowshelf                tonemap_vaapi
bwdif_cuda              lumakey                 tpad
bwdif_vulkan            lut                     transpose
cas                     lut1d                   transpose_cuda
ccrepack                lut2                    transpose_opencl
cellauto                lut3d                   transpose_vaapi
channelmap              lutrgb                  transpose_vulkan
channelsplit            lutyuv                  treble
chorus                  mandelbrot              tremolo
chromaber_vulkan        maskedclamp             trim
chromahold              maskedmax               unpremultiply
chromakey               maskedmerge             unsharp
chromakey_cuda          maskedmin               unsharp_opencl
chromanr                maskedthreshold         untile
chromashift             maskfun                 uspp
ciescope                mcdeint                 v360
codecview               mcompand                v360_vulkan
color                   median                  vaguedenoiser
color_vulkan            mergeplanes             varblur
colorbalance            mestimate               vectorscope
colorchannelmixer       mestimate_d3d12         vflip
colorchart              metadata                vflip_vulkan
colorcontrast           midequalizer            vfrdet
colorcorrect            minterpolate            vibrance
colordetect             mix                     vibrato
colorhold               monochrome              vidstabdetect
colorize                morpho                  vidstabtransform
colorkey                movie                   vif
colorkey_opencl         mpdecimate              vignette
colorlevels             mptestsrc               virtualbass
colormap                msad                    vmafmotion
colormatrix             multiply                volume
colorspace              negate                  volumedetect
colorspace_cuda         nlmeans                 vpp_amf
colorspectrum           nlmeans_opencl          vpp_qsv
colortemperature        nlmeans_vulkan          vqe_amf
compand                 nnedi                   vstack
compensationdelay       noformat                vstack_qsv
concat                  noise                   vstack_vaapi
convolution             normalize               w3fdif
convolution_opencl      null                    waveform
convolve                nullsink                weave
copy                    nullsrc                 whisper
corr                    ocio                    xbr
cover_rect              openclsrc               xcorrelate
crop                    oscilloscope            xfade
cropdetect              overlay                 xfade_opencl
crossfeed               overlay_cuda            xfade_vulkan
crystalizer             overlay_opencl          xmedian
cue                     overlay_qsv             xpsnr
curves                  overlay_vaapi           xstack
datascope               overlay_vulkan          xstack_qsv
dblur                   owdenoise               xstack_vaapi
dcshift                 pad                     yadif
dctdnoiz                pad_cuda                yadif_cuda
ddagrab                 pad_opencl              yaepblur
deband                  pad_vaapi               yuvtestsrc
deblock                 pal100bars              zmq
decimate                pal75bars               zoneplate
deconvolve              palettegen              zoompan
dedot                   paletteuse              zscale

Enabled bsfs:
aac_adtstoasc           h264_mp4toannexb        pgs_frame_merge
ahx_to_mp2              h264_redundant_pps      prores_metadata
apv_metadata            hapqa_extract           remove_extradata
av1_frame_merge         hevc_metadata           setts
av1_frame_split         hevc_mp4toannexb        showinfo
av1_metadata            imx_dump_header         side_data
chomp                   jpegapp                 smpte436m_to_eia608
dca_core                lcevc_merge             text2movsub
dovi_rpu                lcevc_metadata          trace_headers
dovi_split              media100_to_mjpegb      trim
dts2pts                 mjpeg2jpeg              truehd_core
dump_extradata          mjpega_dump_header      vp9_metadata
dv_error_marker         mov2textsub             vp9_raw_reorder
eac3_core               mpeg2_metadata          vp9_superframe
eia608_to_smpte436m     mpeg4_unpack_bframes    vp9_superframe_split
evc_frame_merge         noise                   vvc_metadata
extract_extradata       null                    vvc_mp4toannexb
filter_units            opus_metadata
h264_metadata           pcm_rechunk

Enabled indevs:
dshow                   lavfi                   openal
gdigrab                 libcdio                 vfwcap

Enabled outdevs:
caca

git-full external libraries' versions: 

amf-headers         1.5.3-1
aom                 v3.15.3-130-gd55e6b33a8
aribb24             v1.0.3-5-g5e9be27
astc-encoder        5.7.0-10-gd0f9138
avisynth+           v3.7.6
cairo               1.18.6-4-g74755964e
chromaprint         1.6.2-1
codec2              1.2.0-108-g310777b1
dav1d               1.5.4-43-g4e3ab21f
davs2               1.7-1-gb41cf11
dvdnav              7.0.0-18-g8147ccd
dvdread             7.1.1-125-g0f30df5
ffnvcodec           n13.1.15.0-4-gf205307
flite               v2.2-55-g6c9f20d
fontconfig          2.18.3-99-gb6cf4b2
freetype            VER-2-15-0-17-g63e7ef2e
frei0r              v1.5-463-g618dde7
fribidi             v1.0.18
game-music-emu      0.6.3-249-gf68963b
gnutls              3.8.13-3
gsm                 1.0.24-1
harfbuzz            15.0.0-119-gb05c7266
ladspa-sdk          1.17-2
lame                3.100-3
lc3                 v1.1.3-11-gf9c127f
lcms2               2.19.1-1
lensfun             v0.3.2-3453-gbc5615d6
libaribcaption      v1.0.0-98-g37dde0f
libass              0.17.5-19-g00fe2ec
libbluray           1.5.1-4-gf33a738
libbs2b             3.1.0
libcaca             0.99.beta20-8
libcdio-paranoia    10.2+2.0.2-2
libilbc             v3.0.4-346-g6adb26d4a4
libjxl              v0.12-snapshot-50-ga16d32d0
liblcevc-dec        4.3.1
libmodplug          0.8.9.0-5
libmysofa           v1.3.1-79-g648eed0
libopencolorio      v1.0.8-961-g22dd9c4f
libplacebo          v7.387.0-6-gc4de47c
librabbitmq         v0.18.1-1-g540e497
librist             v0.2.20-18-ga911bee
libssh              0.12.2-1
libunibreak         7.0-1
libvo-amrwbenc      v0.1.3-7-g884dd24
libvpl              v2.17.0-1-g674d015
libwebp             v1.6.0-362-g1844042
libxml2             v2.15.0-135-g2034036d
ogg                 v1.3.6-7-g06a5e02
openal-soft         latest-1-g1fbc89b
openapv             v1.1.3.0-1-g1b4b2e8
opencl-headers      v2026.05.29-11-g82f6031
opencl-loader       v2026.05.29-7-g007c8e8
opencore-amr        0.1.6-1
openjpeg2           2.5.4-2
openmpt             libopenmpt-0.2.6774-beta20-11217-g52f41d55
opus                v1.6.1-95-gbafd40dc
qrencode            v4.0.0-rc3-102-g715e29f
quirc               v1.2-14-gf2e4271
rav1e               p20250624-8-g31435de
rubberband          v4.0.0-2-ge4296ac
SDL                 release-3.4.0-1699-gbd9f6ca9f
shine               3.1.1-59-gab5e352
snappy              1.3.1-1
sox                 sox-14.4.2-184-gf3094754
speex               Speex-1.2.1-57-gf461ff4
srt                 v1.5.7-18-g9f23902
SVT-AV1             v2.3.0-1415-g054ef9356
SVT-JPEG-XS         v0.10.0
theora              v1.2.0alpha1-224-g28fd5ec
twolame             0.4.0-3
uavs3d              1.2
vaapi               2.11.0.pre1-281-gf052e984
vapoursynth         R82RC1
vidstab             v1.1.0-291-ge2445c4
vmaf                v3.2.1-70-g4611e47a
vorbis              v1.3.7-37-g1b75110b
vpx                 v1.17.0-91-g360f03c2f
vulkan-loader       sdk-0.1.0-4115-gaa6dee83
vvenc               v1.14.0-320-g95100f3
whisper             v1.9.5-257-g482279b8
x264                0.165.3223
x265                4.3-93-g0807b60b
xavs2               1.4
xevd                v0.8.0
xeve                v0.7.1
xvidcore            1.3.7-5
zeromq              4.3.5-5
zimg                release-3.0.6-253-g67e0603
zvbi                v0.2.46

