import java.io.*;
import java.net.*;
import org.json.*;
import java.util.Scanner;
import java.util.Base64;


public class Client {
	public static void main(String[] args) throws UnknownHostException, IOException {
		Socket socket = new Socket("localhost", 5678);
		
		Scanner ler = new Scanner(System.in);
				
		System.out.println("Selecione uma opção:");
		System.out.println("1 - Enviar arquivo");
		System.out.println("2 - Receber arquivo");
		
		int opcao=ler.nextInt();
		
		if (opcao==1) { //Enviar arquivo
			//Criando objeto JSON para inserir dados
			JSONObject js = new JSONObject();
			try {
			js.put("type", "write");
			js.put("file", "arquivo.txt");
			
			//Campo mensagem deve estar na base64
			String msg = "Yey!";
			String msg_b64 = Base64.getEncoder().encodeToString(msg.getBytes());
						
			js.put("msg", msg_b64);
			} catch (JSONException e) {}
			
			//Criando arquivo info.json que sera enviado ao servidor
			
			byte[] bytes = new byte[8192];
			
			FileWriter arquivo = new FileWriter("info.json");
			arquivo.write(js.toString());
				
			String json_string = js.toString();
			
			InputStream entrada = new FileInputStream(json_string);
			OutputStream saida = socket.getOutputStream();
					
			int cont;
			while ((cont = entrada.read(bytes)) > 0) {
				saida.write(bytes, 0, cont);
				
			entrada.close();
			saida.close();
			}
		}
		
		else if (opcao==2) { //Receber arquivo
			
			byte [] bytes = new byte [8192];
			
			InputStream entrada = socket.getInputStream();
			OutputStream s = new FileOutputStream("info.json");
			BufferedOutputStream buffer = new BufferedOutputStream(s);
			
			int i,j=0;
			
			do {
				i = entrada.read(bytes, j, (bytes.length-j));
				if (i >= 0)
					j += i;
			} while (i > -1);
			
			buffer.write(bytes, 0, j);
			buffer.flush();
			
			buffer.close();
			entrada.close();
			s.close();
		}
		
		else {
			System.out.println("Opcao invalida! Encerrando conexao...");
		}
		socket.close();
	}
}
