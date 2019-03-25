$(function () {
    'use strict';

    //定义变量
    let console = window.console || { log: function () {} };
    let URL = window.URL || window.webkitURL;
    let $image = $('#image');
    let $download = $('#download');
    let $dataX = $('#dataX');
    let $dataY = $('#dataY');
    let $dataHeight = $('#dataHeight');
    let $dataWidth = $('#dataWidth');
    let $dataRotate = $('#dataRotate');
    let $dataScaleX = $('#dataScaleX');
    let $dataScaleY = $('#dataScaleY');
    let options = {
        //设置裁剪比
        aspectRatio: NaN,
        preview: '.img-preview',
        crop: function (e) {
            $dataX.val(Math.round(e.detail.x));
            $dataY.val(Math.round(e.detail.y));
            $dataHeight.val(Math.round(e.detail.height));
            $dataWidth.val(Math.round(e.detail.width));
            $dataRotate.val(e.detail.rotate);
            $dataScaleX.val(e.detail.scaleX);
            $dataScaleY.val(e.detail.scaleY);
        }
    };
    let originalImageURL = $image.attr('src');
    let uploadedImageName = 'cropped.jpg';
    let uploadedImageType = 'image/jpeg';
    let uploadedImageURL;


    //获取页面传值所获得的图片url并加载
    let previewUrl =  getQueryString("preview");

    if(previewUrl == "" || previewUrl == null || previewUrl == undefined){
        alert("您并未点开表情包哦！")
    }
    else{
        $image.attr("src", previewUrl);
        originalImageURL = $image.attr('src');
        //$image.attr('crossOrigin', 'anonymous');
    }


    // Tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // Cropper
    $image.on({
        ready: function (e) {
        },
        cropstart: function (e) {
        },
        cropmove: function (e) {
        },
        cropend: function (e) {
        },
        crop: function (e) {
        },
        zoom: function (e) {

        }
    }).cropper(options);

    // Buttons
    if (!$.isFunction(document.createElement('canvas').getContext)) {
        $('button[data-method="getCroppedCanvas"]').prop('disabled', true);
    }

    if (typeof document.createElement('cropper').style.transition === 'undefined') {
        $('button[data-method="rotate"]').prop('disabled', true);
        $('button[data-method="scale"]').prop('disabled', true);
    }

    // Download
    if (typeof $download[0].download === 'undefined') {
        $download.addClass('disabled');
    }

    // Options
    $('.docs-toggles').on('change', 'input', function () {
        var $this = $(this);
        var name = $this.attr('name');
        var type = $this.prop('type');
        var cropBoxData;
        var canvasData;

        if (!$image.data('cropper')) {
            return;
        }

        if (type === 'checkbox') {
            options[name] = $this.prop('checked');
            cropBoxData = $image.cropper('getCropBoxData');
            canvasData = $image.cropper('getCanvasData');

            options.ready = function () {
                $image.cropper('setCropBoxData', cropBoxData);
                $image.cropper('setCanvasData', canvasData);
            };
        } else if (type === 'radio') {
            options[name] = $this.val();
        }

        $image.cropper('destroy').cropper(options);
    });

    // Methods
    $('.docs-buttons').on('click', '[data-method]', function () {
        var $this = $(this);
        var data = $this.data();
        var cropper = $image.data('cropper');
        var cropped;
        var $target;
        var result;

        if ($this.prop('disabled') || $this.hasClass('disabled')) {
            return;
        }

        if (cropper && data.method) {
            data = $.extend({}, data); // Clone a new one

            if (typeof data.target !== 'undefined') {
                $target = $(data.target);

                if (typeof data.option === 'undefined') {
                    try {
                        data.option = JSON.parse($target.val());
                    } catch (e) {
                        console.log(e.message);
                    }
                }
            }

            cropped = cropper.cropped;

            switch (data.method) {
                case 'rotate':
                    if (cropped && options.viewMode > 0) {
                        $image.cropper('clear');
                    }

                    break;

                case 'getCroppedCanvas':
                    if (uploadedImageType === 'image/jpeg') {
                        if (!data.option) {
                            data.option = {};
                        }

                        data.option.fillColor = '#fff';
                    }

                    break;
            }

            $image.attr("crossOrigin",'Anonymous');
            result = $image.cropper(data.method, data.option, data.secondOption);

            switch (data.method) {
                case 'rotate':
                    if (cropped && options.viewMode > 0) {
                        $image.cropper('crop');
                    }

                    break;

                case 'scaleX':
                case 'scaleY':
                    $(this).data('option', -data.option);
                    break;

                case 'getCroppedCanvas':
                    if (result) {
                        // Bootstrap's Modal
                        $('#getCroppedCanvasModal').modal()
                            .find('.modal-body').html(result);

                        if (!$download.hasClass('disabled')) {
                            $download.download = uploadedImageName;

                            //let cacheSrc = URL.createObjectURL(this.response);
                            // alert(result);
                            // console.log(result);

                            $image.attr("crossOrigin",'Anonymous');
                            //$download.attr('href', result.toDataURL(uploadedImageType));
                            // $image.onload = function(){//图片加载完，再draw 和 toDataURL
                            //     alert("fuck");
                            //
                            // };

                        }
                    }

                    break;

                case 'destroy':
                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                        uploadedImageURL = '';
                        $image.attr('src', originalImageURL);
                    }

                    break;
            }

            if ($.isPlainObject(result) && $target) {
                try {
                    $target.val(JSON.stringify(result));
                } catch (e) {
                    console.log(e.message);
                }
            }
        }
    });

    // Keyboard
    $(document.body).on('keydown', function (e) {
        if (e.target !== this || !$image.data('cropper') || this.scrollTop > 300) {
            return;
        }

        switch (e.which) {
            case 37:
                e.preventDefault();
                $image.cropper('move', -1, 0);
                break;

            case 38:
                e.preventDefault();
                $image.cropper('move', 0, -1);
                break;

            case 39:
                e.preventDefault();
                $image.cropper('move', 1, 0);
                break;

            case 40:
                e.preventDefault();
                $image.cropper('move', 0, 1);
                break;
        }
    });

    // Import image
    var $inputImage = $('#inputImage');

    if (URL) {
        $inputImage.change(function () {
            var files = this.files;
            var file;

            if (!$image.data('cropper')) {
                return;
            }

            if (files && files.length) {
                file = files[0];

                if (/^image\/\w+$/.test(file.type)) {
                    uploadedImageName = file.name;
                    uploadedImageType = file.type;

                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                    }

                    uploadedImageURL = URL.createObjectURL(file);
                    $image.cropper('destroy').attr('src', uploadedImageURL).cropper(options);
                    $inputImage.val('');
                } else {
                    window.alert('Please choose an image file.');
                }
            }
        });
    } else {
        $inputImage.prop('disabled', true).parent().addClass('disabled');
    }



});


//获取url传递参数，js获取url？号后面的参数
function getQueryString(name) {
    let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    let r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}




