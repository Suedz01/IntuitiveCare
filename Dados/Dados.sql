DO $$ 
BEGIN
    FOR i IN 1..4 LOOP
        EXECUTE format('
            CREATE TABLE IF NOT EXISTS "%sT2023" (
                date DATE NOT NULL,
                reg_ans VARCHAR(20) NOT NULL,
                cd_conta_contabil VARCHAR(50) NOT NULL,
                descricao TEXT NOT NULL,
                vl_saldo_inicial NUMERIC(15,2) NOT NULL,
                vl_saldo_final NUMERIC(15,2) NOT NULL
            );', i);

        EXECUTE format('
            CREATE TABLE IF NOT EXISTS "%sT2024 (
                date DATE NOT NULL,
                reg_ans VARCHAR(20) NOT NULL,
                cd_conta_contabil VARCHAR(50) NOT NULL,
                descricao TEXT NOT NULL,
                vl_saldo_inicial NUMERIC(15,2) NOT NULL,
                vl_saldo_final NUMERIC(15,2) NOT NULL
            );', i);
    END LOOP;
END $$;






CREATE TABLE ultimo_trimestre AS
SELECT 
    reg_ans,
    date,
    descricao,
    SUM(vl_saldo_final) AS total_despesas
FROM 
    "4T2024"
WHERE 
    descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
GROUP BY 
    reg_ans,
    date,
    descricao
ORDER BY 
    total_despesas DESC
LIMIT 10;
SELECT * FROM ultimo_trimestre;





CREATE TABLE ultimo_ano AS
SELECT 
    reg_ans,
    date,
    descricao,
    SUM(vl_saldo_final) AS total_despesas
FROM 
    (
        SELECT reg_ans, date, descricao, vl_saldo_final
        FROM "1T2024"
        WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
        
        UNION ALL
        
        SELECT reg_ans, date, descricao, vl_saldo_final
        FROM "2T2024"
        WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
        
        UNION ALL
        
        SELECT reg_ans, date, descricao, vl_saldo_final
        FROM "3T2024"
        WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
        
        UNION ALL
        
        SELECT reg_ans, date, descricao, vl_saldo_final
        FROM "4T2024"
        WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE'
    ) AS combined_data
GROUP BY reg_ans, date, descricao
ORDER BY total_despesas DESC
LIMIT 10;
SELECT * FROM ultimo_ano;
