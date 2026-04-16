package com.example.hamburgueriaz;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    // Views
    private EditText  editNome;
    private CheckBox  checkBacon, checkQueijo, checkOnionRings;
    private TextView  textQuantidade, textResumo, textTotal;

    // Controle de quantidade
    private int quantidade = 0;

    // Preços
    private static final double PRECO_BASE   = 20.0;
    private static final double PRECO_BACON  = 2.0;
    private static final double PRECO_QUEIJO = 2.0;
    private static final double PRECO_ONION  = 3.0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar views
        editNome        = findViewById(R.id.editNome);
        checkBacon      = findViewById(R.id.checkBacon);
        checkQueijo     = findViewById(R.id.checkQueijo);
        checkOnionRings = findViewById(R.id.checkOnionRings);
        textQuantidade  = findViewById(R.id.textQuantidade);
        textResumo      = findViewById(R.id.textResumo);
        textTotal       = findViewById(R.id.textTotal);
        Button btnSomar = findViewById(R.id.btnSomar);
        Button btnSubtrair = findViewById(R.id.btnSubtrair);
        Button btnEnviar = findViewById(R.id.btnEnviarPedido);

        // Atualiza o footer ao marcar/desmarcar adicionais
        checkBacon.setOnCheckedChangeListener((b, c)      -> atualizarFooter());
        checkQueijo.setOnCheckedChangeListener((b, c)     -> atualizarFooter());
        checkOnionRings.setOnCheckedChangeListener((b, c) -> atualizarFooter());

        // Botões quantidade
        btnSomar.setOnClickListener(v    -> somar());
        btnSubtrair.setOnClickListener(v -> subtrair());

        // Botão enviar
        btnEnviar.setOnClickListener(v -> enviarPedido());
    }

    // ── Etapa 5: Somar ────────────────────────────────────────────────────────
    private void somar() {
        quantidade++;
        textQuantidade.setText(String.valueOf(quantidade));
        atualizarFooter();
    }

    // ── Etapa 5: Subtrair (sem negativos) ────────────────────────────────────
    private void subtrair() {
        if (quantidade > 0) {
            quantidade--;
            textQuantidade.setText(String.valueOf(quantidade));
            atualizarFooter();
        }
    }

    // ── Calcular total ────────────────────────────────────────────────────────
    private double calcularTotal() {
        double adicionais = 0;
        if (checkBacon.isChecked())      adicionais += PRECO_BACON;
        if (checkQueijo.isChecked())     adicionais += PRECO_QUEIJO;
        if (checkOnionRings.isChecked()) adicionais += PRECO_ONION;
        return (PRECO_BASE + adicionais) * quantidade;
    }

    // ── Atualiza footer em tempo real ─────────────────────────────────────────
    private void atualizarFooter() {
        double total = calcularTotal();

        // Monta linha de resumo dos adicionais
        StringBuilder adicionais = new StringBuilder();
        if (checkBacon.isChecked())      adicionais.append("+ Bacon\n");
        if (checkQueijo.isChecked())     adicionais.append("+ Queijo\n");
        if (checkOnionRings.isChecked()) adicionais.append("+ Onion Rings\n");

        String resumo = quantidade + "x Hambúrguer\n" +
                (adicionais.length() > 0 ? adicionais.toString() : "");

        textResumo.setText(resumo.trim().isEmpty() ? "Nenhum item selecionado" : resumo.trim());
        textTotal.setText(String.format(Locale.getDefault(), "R$ %.2f", total));
    }

    // ── Etapas 6 e 7: Montar resumo completo e enviar por e-mail ─────────────
    private void enviarPedido() {

        // Validação do nome (campo obrigatório)
        String nome = editNome.getText().toString().trim();
        if (nome.isEmpty()) {
            Toast.makeText(this, "Por favor, informe o nome!", Toast.LENGTH_SHORT).show();
            editNome.requestFocus();
            return;
        }

        if (quantidade == 0) {
            Toast.makeText(this, "Selecione ao menos 1 hambúrguer!", Toast.LENGTH_SHORT).show();
            return;
        }

        boolean temBacon  = checkBacon.isChecked();
        boolean temQueijo = checkQueijo.isChecked();
        boolean temOnion  = checkOnionRings.isChecked();
        double  total     = calcularTotal();

        // Resumo completo para o e-mail
        String resumoEmail =
                "Nome do cliente: " + nome + "\n" +
                        "Tem Bacon? "       + (temBacon  ? "Sim" : "Não") + "\n" +
                        "Tem Queijo? "      + (temQueijo ? "Sim" : "Não") + "\n" +
                        "Tem Onion Rings? " + (temOnion  ? "Sim" : "Não") + "\n" +
                        "Quantidade: "      + quantidade + "\n" +
                        "Preço final: R$ "  + String.format(Locale.getDefault(), "%.2f", total);

        // Exibe no footer
        textResumo.setText(resumoEmail);
        textTotal.setText(String.format(Locale.getDefault(), "R$ %.2f", total));

        // ── Etapa 7: Intent de e-mail ─────────────────────────────────────────
        Intent intent = new Intent(Intent.ACTION_SENDTO);
        intent.setData(Uri.parse("mailto:"));
        intent.putExtra(Intent.EXTRA_SUBJECT, "Pedido de " + nome);
        intent.putExtra(Intent.EXTRA_TEXT, resumoEmail);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
    }
}
