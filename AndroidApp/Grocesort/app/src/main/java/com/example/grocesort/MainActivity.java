package com.example.grocesort;
//Codigo de Rayner Gabu
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.CookieManager;
import android.webkit.CookieSyncManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;
//Codigo de Rayner Gabu
import androidx.appcompat.app.AppCompatActivity;
//Codigo de Rayner Gabu
public class MainActivity extends AppCompatActivity {
    //Codigo de Rayner Gabu
    private WebView myWebView;
    //Codigo de Rayner Gabu
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setTheme(R.style.Base_Theme_Grocesort);
        setContentView(R.layout.activity_main);
//Codigo de Rayner Gabu
        myWebView = findViewById(R.id.web1);
//Codigo de Rayner Gabu
        // Configuraciones de WebSettings
        WebSettings settings = myWebView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccessFromFileURLs(true);
        settings.setAllowUniversalAccessFromFileURLs(true);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        myWebView.addJavascriptInterface(new WebAppInterface(), "Android");
//Codigo de Rayner Gabu
        // Configuraciones del CookieManager
        CookieManager cookieManager = CookieManager.getInstance();
        cookieManager.setAcceptCookie(true);
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
            cookieManager.setAcceptThirdPartyCookies(myWebView, true);
        }
//Codigo de Rayner Gabu
        // Iniciar la sincronización de cookies
        CookieSyncManager.createInstance(this);
//Codigo de Rayner Gabu
        // Cargar la URL en el WebView
        myWebView.loadUrl("https://www.raynergrocesort.rf.gd/paginas/paginas/secciones.php");
        myWebView.setWebViewClient(new MyWebViewClient() {
            @Override
            public void onPageFinished(WebView view, String url) {
                pincharBotonAceptarCookies();
                ocultarElementoPorId(myWebView, "androidTest");
//Codigo de Rayner Gabu
                agregarBotonEncima();
                ocultarLogos();
            }
        });
    }
    //Codigo de Rayner Gabu
    // Método para pinchar el botón "Aceptar" mediante JavaScript
    private void pincharBotonAceptarCookies() {
        // Código JavaScript para hacer clic en el botón con id "btnAceptarCookies"
        String javascriptCode = "document.getElementById('btnAceptarCookies').click();";

        // Ejecutar el código JavaScript en el WebView
        myWebView.evaluateJavascript(javascriptCode, null);
    }
    //Codigo de Rayner Gabu
    private void ocultarElementoPorId(final WebView webView, final String id) {
        String javascriptCode = "var elemento = document.getElementById('" + id + "');" +
                "if (elemento) {" +
                "    elemento.style.display = 'none';" +
                "}";
        webView.evaluateJavascript(javascriptCode, null);
    }
    //Codigo de Rayner Gabu
    private void ocultarLogos() {
        String javascriptCode = "var logos = document.getElementsByClassName('logo'); " +
                "for (var i = 0; i < logos.length; i++) { " +
                "    logos[i].style.display = 'none'; " +
                "}";
        // Ejecutar el código JavaScript en el WebView
        myWebView.evaluateJavascript(javascriptCode, null);
    }
    //Codigo de Rayner Gabu
    public class WebAppInterface {
        //Codigo de Rayner Gabu
        @JavascriptInterface
        public void showAddedToCartToast() {
            Toast.makeText(MainActivity.this, "Añadido a cesta. ≡ > Cesta para verla", Toast.LENGTH_SHORT).show();
        }
    }
    //Codigo de Rayner Gabu
    private void agregarBotonEncima() {
        // Código JavaScript para agregar el botón antes del elemento con clase "ms-5" y "mt-5"
        String javascriptCode = "var newButton = document.createElement('button'); " +
                "newButton.type = 'button'; " +
                "newButton.className = 'btn btn-primary'; " + "newButton.style.paddingLeft = '25%'; " + "newButton.style.paddingRight = '25%'; " +
                "newButton.innerHTML = 'Volver atrás'; " +
                "var link = document.createElement('a'); " +
                "link.href = 'secciones.php'; " +
                "link.appendChild(newButton); " +
                "var breadcrumbNav = document.querySelector('.ms-5.mt-5[aria-label=breadcrumb]'); " +
                "breadcrumbNav.appendChild(link);";
    //Codigo de Rayner Gabu
        // Ejecutar el código JavaScript en el WebView
        myWebView.evaluateJavascript(javascriptCode, null);
    }
    //Codigo de Rayner Gabu
    @Override
    public void onBackPressed() {
        if (myWebView.canGoBack()) {
            myWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }
    //Codigo de Rayner Gabu
    @Override
    protected void onDestroy() {
        super.onDestroy();
        //Codigo de Rayner Gabu
        // Sincronizar las cookies antes de destruir la actividad
        CookieSyncManager.getInstance().sync();
        //Codigo de Rayner Gabu
        // Guardar las cookies en SharedPreferences
        String cookies = CookieManager.getInstance().getCookie("https://www.raynergrocesort.rf.gd");
        SharedPreferences preferences = getPreferences(MODE_PRIVATE);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString("saved_cookies", cookies);
        editor.apply();
    }
    //Codigo de Rayner Gabu
    private class MyWebViewClient extends WebViewClient {
        @Override
        public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
            Uri uri = request.getUrl();
            String url = uri.toString();
            //Codigo de Rayner Gabu
            // Verificar si el enlace lleva a la página que quieres abrir en el navegador
            if (url.endsWith("sobremi/index.html") || "https://www.google.com/maps/search/alcampo/".equals(url) ||
                    "https://www.google.com/maps/search/ahorramas/".equals(url) ||
                    "https://www.google.com/maps/search/carrefour/".equals(url) ||
                    "https://www.google.com/maps/search/dia/".equals(url) ||
                    "https://www.google.com/maps/search/eroski/".equals(url) ||
                    "https://www.google.com/maps/search/mercadona".equals(url)) {
                // Abrir en el navegador del dispositivo
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                startActivity(intent);
                return true; // Evitar que el WebView maneje la carga de la URL
            }
            //Codigo de Rayner Gabu
            if (url.substring(0, Math.min(url.length(), 20)).equals("https://www.ahorrama")
                    || "https://www.compraon".equals(url.substring(0, Math.min(url.length(), 20)))
                    || "https://www.carrefou".equals(url.substring(0, Math.min(url.length(), 20)))
                    || "https://www.dia.es/".equals(url.substring(0, Math.min(url.length(), 19)))
                    || "https://supermercado".equals(url.substring(0, Math.min(url.length(), 20)))
                    || "https://tienda.merca".equals(url.substring(0, Math.min(url.length(), 20)))) {
                // Tu código aquí
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                startActivity(intent);
                return true;
            }
            //Codigo de Rayner Gabu
            // Permitir que el WebView maneje la carga de la URL
            return false;
        }
    }
//Codigo de Rayner Gabu
}